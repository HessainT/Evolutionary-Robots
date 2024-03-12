#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:36:55 2024

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

#%% Sensor class constructor
class SENSOR:
    def __init__(self, linkName):
        
        # Assign linkName
        self.linkName = linkName
                
        # Create arrays to save sensor values to
        self.values = np.zeros(c.STEPS) #Create numpy array with same length as steps
        
    #%% Get value function
    def Get_Value(self,step):
        # Get sensor values
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    #%% Save values
    def Save_Values(self, filename):
        np.save(filename, self.values)