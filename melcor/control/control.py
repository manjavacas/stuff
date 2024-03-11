#!/usr/bin/python3

import subprocess
import numpy as np

MODEL_PATH = 'SAMPLE.inp'
EDF_PATH = 'PRESSURES.DAT'

TARGET_PRESSURE = 101235

CONTROL_HORIZON = 20

CF_TEMPLATE = 'CF00200 CONTROLLER MULTIPLY 2 '


def edit_cf(new_velocity):
    with open(MODEL_PATH, 'r+') as f:
        lines = f.readlines()
        edit_pos_cf = -1
        edit_pos_time = -1

        for i, line in enumerate(lines):
            if 'CF002' in line:
                edit_pos_cf = i
            if 'TEND' in line:
                edit_pos_time = i
                current_sim_time = int(line.split()[1])

        if edit_pos_cf != -1:
            lines[edit_pos_cf] = CF_TEMPLATE + str(new_velocity) + '\n'
            lines[edit_pos_time] = 'TEND ' + \
                str(current_sim_time + CONTROL_HORIZON) + '\n'
            f.seek(0)
            f.writelines([line.strip() + '\n' for line in lines])
            f.truncate()
            print('[INFO] Control action applied!')
        else:
            print('[ERROR] Control function not found!')
            exit()


def apply_sigmoid(pressure):
    k = 0.01
    return 2 / (1 + np.exp(-k * (pressure - TARGET_PRESSURE))) - 1


# First execution
subprocess.call(['make', 'run'])

# Iterative control
while True:

    with open(EDF_PATH, 'r') as f:
        last_record = f.readlines()[-1]
        values = np.array(last_record.split(), dtype=np.float32)

    if values[1] < TARGET_PRESSURE:
        edit_cf(-1.0)
    elif values[2] < TARGET_PRESSURE:
        edit_cf(1.0)

    # new_velocity = apply_sigmoid(values[1])
    # edit_cf(new_velocity)

    subprocess.call(['make', 'cor'])
