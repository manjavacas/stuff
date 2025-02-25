import logging

import os
import shutil
import glob
import pickle
import sinergym
import csv

import gymnasium as gym
import numpy as np

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


def wrap_env(environment, mean_path=None, var_path=None):

    if mean_path and var_path:
        environment = NormalizeObservation(
            environment, mean=mean_path, var=var_path)
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
            'plr_current']
    )
    return environment

# -------------------------------------- EVALUATION ------------------------------#


model_path = 'best_model.zip'
mean_file_path = 'mean.txt'
var_file_path = 'var.txt'

EVAL_EPISODES = 1
SEEDS = range(10)

ENV_ID = 'Eplus-radiant_case1_heating-stockholm-continuous-stochastic-v1'

model = TD3.load(model_path)

mean_path = mean_file_path
var_path = var_file_path

env = gym.make(ENV_ID, env_name='DEPLOY')
env = wrap_env(env, mean_path, var_path)


for seed in SEEDS:
    for ep in range(EVAL_EPISODES):

        obs, _ = env.reset(seed)
        env.action_space.seed(seed)

        truncated = terminated = False

        while not (terminated or truncated):
            a, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, _ = env.step(a)

env.close()
