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

#%% Motor class constructor
class MOTOR:
    def __init__(self, jointName):
        
        #Assign jointName
        self.jointName = jointName
        
        #self.Prepare_To_Act()

#%% Prepare to act function
    # def Prepare_To_Act(self):
    #     self.amplitude = c.amplitude
    #     self.frequency = c.frequency
    #     self.offset = c.phase
        
    #     # Set different frequencies based on jointName
    #     if self.jointName == "Torso_FrontLeg":    #Normal frequency for first motor
    #         self.frequency = c.frequency
    #     elif self.jointName == "Torso_BackLeg":  #Half frequency for second motor
    #         self.frequency = c.frequency / 2
    #     else:
    #         self.frequency = c.frequency   #All other frequencies are normal
        
        
    #     # Create time values for motor controls
    #     self.time_values = np.linspace(c.lower_time_bound, c.upper_time_bound, c.STEPS) #Create array for range of values and subdivisions (STEPS)

    #     # Create motor values that will be used to control robot
    #     self.motor_values = self.amplitude * np.sin(self.frequency * self.time_values) + self.offset #Create the sin function   

#%% Set_Value method
    def Set_Value(self, robotId, desiredAngle):
        # Backleg motor
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.max_force) 
    #%% Save values
    # def Save_Values(self, filename):
    #     np.save(filename, self.motor_values)
    
