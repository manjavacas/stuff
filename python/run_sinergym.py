import sinergym
import logging

from datetime import datetime
from stable_baselines3 import PPO

import gymnasium as gym
import numpy as np

from sinergym.utils.callbacks import LoggerEvalCallback
from sinergym.utils.logger import TerminalLogger
from sinergym.utils.rewards import BalancedRewardV2
from sinergym.utils.wrappers import (
    LoggerWrapper,
    NormalizeAction,
    NormalizeObservation,
    ReduceObservationWrapper,
    CSVLogger,
    ExtremeFlowControlWrapper
)

# --------------------------------- SETTINGS -------------------------------- #

TRAIN_EPISODES = 150
EVAL_FREQ = 5
EVAL_EPISODES = 1

ENV_ID = 'Eplus-radiant_case2_heating-stockholm-continuous-stochastic-v1'

output_dir = ENV_ID + '-res1/'

best_model_path = output_dir + 'evaluation/best_model.zip'
mean_file_path = output_dir + 'evaluation/mean.txt'
var_file_path = output_dir + 'evaluation/var.txt'

# --------------------------------- LOGGING --------------------------------- #

terminal_logger = TerminalLogger()
logger = terminal_logger.getLogger(
    name='MAIN',
    level=logging.INFO
)

# --------------------------------- WRAPPERS -------------------------------- #


def wrap_env(environment, mean_path=None, var_path=None):
    """
    Modifies the environment with various wrappers, including normalization and logging.
    Args:
        environment: The environment to wrap.
        mean_path: Path to the mean file for normalization (optional).
        var_path: Path to the variance file for normalization (optional).
    Returns:
        Wrapped environment.
    """
    environment = ExtremeFlowControlWrapper(environment)  # case 2 only
    if mean_path and var_path:
        environment = NormalizeObservation(
            env=environment,
            automatic_update=False,
            mean=mean_path,
            var=var_path
        )
    else:
        environment = NormalizeObservation(environment)
    environment = NormalizeAction(environment)
    environment = LoggerWrapper(environment)
    environment = CSVLogger(environment)
    environment = ReduceObservationWrapper(
        environment,
        obs_reduction=[
            'radiant_hvac_outlet_temperature_living',
            'radiant_hvac_outlet_temperature_kitchen',
            'radiant_hvac_outlet_temperature_bed1',
            'radiant_hvac_outlet_temperature_bed2',
            'radiant_hvac_outlet_temperature_bed3',
            'flow_rate_living',
            'flow_rate_kitchen',
            'flow_rate_bed1',
            'flow_rate_bed2',
            'flow_rate_bed3',
            'heat_source_load_side_heat_transfer_rate',
            'heat_source_load_side_mass_flow_rate',
            'crf',
            'heat_cap_mod',
            'cop_plr_mod',
            'cop_temp_mod',
            'plr_current'
        ]
    )
    return environment

# --------------------------------- ENVIRONMENT ----------------------------- #


reward_kwargs = {
    "temperature_variables": ["air_temperature_living",
                              "air_temperature_kitchen",
                              "air_temperature_bed1",
                              "air_temperature_bed2",
                              "air_temperature_bed3"],
    "energy_variables": ["heat_source_electricity_rate"],
    "range_comfort_winter": [19.5, 22.0],
    "range_comfort_summer": [19.5, 22.0],
    "energy_weight": 0.75,
}

env_conf = {
    'timesteps_per_hour': 12,
    'north_axis': 270
}

env = wrap_env(
    gym.make(
        ENV_ID,
        reward=BalancedRewardV2,
        config_params=env_conf,
        reward_kwargs=reward_kwargs
    )
)

# ----------------------------- EVALUATION ENVIRONMENT ---------------------- #

eval_env = wrap_env(
    gym.make(
        ENV_ID,
        reward=BalancedRewardV2,
        config_params=env_conf,
        reward_kwargs=reward_kwargs
    )
)

eval_callback = LoggerEvalCallback(
    train_env=env,
    eval_env=eval_env,
    n_eval_episodes=EVAL_EPISODES,
    eval_freq_episodes=EVAL_FREQ,
    deterministic=True
)

# ------------------------------ MODEL TRAINING ----------------------------- #

model_params = {
    'batch_size': 2048
}

model = PPO('MlpPolicy', env, verbose=1, **model_params)

timesteps = TRAIN_EPISODES * env.get_wrapper_attr('timestep_per_episode')

model.learn(total_timesteps=timesteps, callback=eval_callback)

# ---------------------------------- TESTING -------------------------------- #

best_model = PPO.load(best_model_path)

test_env = wrap_env(
    gym.make(
        ENV_ID,
        reward=BalancedRewardV2,
        config_params=env_conf,
        reward_kwargs=reward_kwargs
    ),
    mean_path=mean_file_path,
    var_path=var_file_path
)

test_episodes = 10
for episode in range(test_episodes):
    obs, _ = test_env.reset()
    done = trunc = False
    total_reward = 0
    while not (done or trunc):
        action, _ = best_model.predict(obs, deterministic=True)
        obs, reward, done, trunc, info = test_env.step(action)
        total_reward += reward
    print(f'Ep. {episode + 1}: Total reward = {total_reward}')
