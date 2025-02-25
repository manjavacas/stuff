import logging

import os
import shutil

import gymnasium as gym
import sinergym

from sys import argv

from sinergym.utils.callbacks import LoggerEvalCallback
from sinergym.utils.logger import TerminalLogger
from sinergym.utils.wrappers import (
    LoggerWrapper,
    NormalizeAction,
    NormalizeObservation,
    ReduceObservationWrapper,
    CSVLogger)

from stable_baselines3 import TD3

# ------------------------------------ LOGGER -----------------------------------#

terminal_logger = TerminalLogger()
logger = terminal_logger.getLogger(
    name='MAIN',
    level=logging.INFO
)

# ----------------------------------- WRAPPERS ----------------------------------#


def wrap_env(environment):
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
            'plr_current']
    )
    return environment

# -------------------------------------- TRAINING ------------------------------#


TRAIN_EPISODES = 30
EVAL_EPISODES = 1
EVAL_FREQ = 10

ENV_ID = 'Eplus-radiant_case1_heating-stockholm-continuous-stochastic-v1'

# ------ TRAINING ENVIRONMENT ------ #

env = gym.make(ENV_ID, env_name='TRAIN')
env = wrap_env(env)

# ----- EVALUATION ENVIRONMENT ----- #

eval_env = gym.make(ENV_ID, env_name='EVAL')
eval_env = wrap_env(eval_env)

eval_callback = LoggerEvalCallback(
    eval_env=eval_env,
    train_env=env,
    n_eval_episodes=EVAL_EPISODES,
    eval_freq_episodes=EVAL_FREQ,
    deterministic=True)

# --------- MODEL TRAINING --------- #

model = TD3('MlpPolicy', env)

train_timesteps = TRAIN_EPISODES * env.get_wrapper_attr('timestep_per_episode')
model.learn(total_timesteps=train_timesteps, callback=eval_callback)

# ----- SAVE MODEL AND OUTPUTS ----- #

save_folder_path = 'td3_train'

try:
    os.mkdir(save_folder_path)
except OSError as error:
    print(f"Error creating '{save_folder_path}': {error}")

model.save(os.path.join(save_folder_path, 'last_model'))

source_path = os.getcwd()

if not os.path.exists(save_folder_path):
    os.makedirs(save_folder_path)

for folder in os.listdir(source_path):
    folder_path = os.path.join(source_path, folder)

    if os.path.isdir(folder_path) and folder.startswith('Eplus-env-'):
        target_path = os.path.join(save_folder_path, folder)
        shutil.move(folder_path, target_path)

print('Train finished!')
