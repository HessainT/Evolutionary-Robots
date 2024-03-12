#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:43:58 2024

@author: hessain
"""
#%% Import stuff
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import random
import constants as c

#%%
class WORLD:
    def __init__(self):
        
        # Load  the simulation
        self.planeId = p.loadURDF("plane.urdf")  # Read in the plane
        p.loadSDF("world.sdf")