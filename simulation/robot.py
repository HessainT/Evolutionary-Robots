#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:43:59 2024

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
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

#%%
class ROBOT:
    #%% Initialization
    def __init__(self, solutionID):
        
        self.ID = solutionID
        
        self.robotId = p.loadURDF("body.urdf")   # Read in the robot
        pyrosim.Prepare_To_Simulate(self.robotId) #Set up sensor
        
        # Call prepare to sense function
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
        #Creates a neural network
        self.nn = NEURAL_NETWORK("brain"+ self.ID +".nndf")
        
        #Remove brain file after use
        os.system("rm brain" + self.ID +".nndf")
        
        
    #%% Prepare to sense
    def Prepare_To_Sense(self):
        self.sensors = {}   #Dictionary with sensors
        
        # Loop to add sensors
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            #Create an instance of SENSOR class for each link
            self.sensors[linkName] = SENSOR(linkName)
    
    #%% Sense function
    def Sense(self,step):
        for sensor_name, sensor in self.sensors.items():
            sensor.Get_Value(step)
            
    #%% Prepare to act function
    def Prepare_To_Act(self):
        self.motors = {} #Dictionary with motors

        # Loop to add motors
        for jointName in pyrosim.jointNamesToIndices:

            #Create an instance of MOTOR class for each link
            self.motors[jointName] = MOTOR(jointName)
            #print(jointName)
    
    #%% Act function
    def Act(self,step):
        for neuronName in self.nn.Get_Neuron_Names():
            
            #Only return name if neuron is a motor neuron
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName) #Retrieve jointName    
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId,desiredAngle)
                
                #print(neuronName, jointName,desiredAngle) #Print name of neuron
        
        #Old form of setting motor values
        # for joint_name, motor in self.motors.items():
        #     motor.Set_Value(self.robotId,step)

    #%% Think function
    def Think(self):
        self.nn.Update()    #Update sensor neurons with latest data
        self.nn.Print()     #Print current neuron values
        
    #%% Get Fitness function
    def Get_Fitness(self):
        
        #Retrieve state of link zero
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        
        #Extract position of link zero from state
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        
        #Extract x position of link zero from position
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        
        # Write xcoord to external file
        with open("tmp"+ str(self.ID) + ".txt", "w") as file:
            file.write(str(self.xCoordinateOfLinkZero))
            
            os.system("mv tmp"+str(self.ID)+".txt fitness"+str(self.ID)+".txt")

        

        

        
