#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:37:51 2024

@author: hessain
"""
#%% Imports
from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import random
import constants as c


#%% Class definition
class SIMULATION:
    def __init__(self):
        # Create an object to handle and draw results to GUI
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # OPTIONAL: Disable sidebars
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
               
        p.setGravity(c.grav_x, c.grav_y, c.grav_z)
        
        self.world = WORLD()    #Create an instance of WORLD() class
        self.robot = ROBOT()    #Create an instance of ROBOT() class
        
    #%% Run Class
    def Run(self):
        # #%% Looping through action
        # # Loop through the action
         for i in range(c.STEPS): 
             p.stepSimulation() # Step
             #Simulated world is "updated"
             
             self.robot.Sense(i)    #Call sense function from robot
             #Robot will sense any "updates" made to the world
             
             self.robot.Think()
             
             self.robot.Act(i)   #Call act function from motor
             #Robot will now act according to any "updates" made to the world
            
             time.sleep(c.sleep_duration) # Sleep for 1/60 second
             # print("1")
             
         # Save sensor values
         for sensor_name, sensor in self.robot.sensors.items():
             sensor.Save_Values("sensor_values_" + sensor_name + ".npy")

         # Save motor values
         for joint_name, motor in self.robot.motors.items():
            motor.Save_Values("motor_values_" + joint_name + ".npy")
     #%% Deconstructor class
    def __del__(self):
        p.disconnect()
        