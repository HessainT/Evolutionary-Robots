#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:51:27 2024

@author: hessain
"""

#%% Import stuff
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import random

#%% Global Constants
# Acceleration Constants
grav_x = 0      # x-grav
grav_y = 0      # y-grav
grav_z = -9.8   # z-grav !!!

# Total simulation STEPS
STEPS = 1000

# Array with time values
lower_time_bound = 0            # Time = 0
upper_time_bound = 2 * np.pi    # Time = 2pi

# Max force (Newtons)
max_force = 25

# Sleep_time (seconds)
sleep_duration = 1/240

#%% BACK leg motor constants
amplitude = np.pi/8    #Amplitude multiplier
frequency = 15.0       #Frequency multiplier
phase = 0.0            #Phase offset


