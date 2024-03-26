#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:10:27 2024

@author: hessain
"""
#%% Imports
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

#%% Solution Class
class SOLUTION:
    def __init__(self):
        
        #Create 3x2 matix w/ random weights in range [0,1]
        self.random_weights = np.random.rand(3,2)
        #print("Random weights (before scaling): ", self.random_weights)
        
        # Scale weights t orange [-1,1]
        self.weights = (self.random_weights * 2) -1
        #print("Random weights (after scaling): ", self.weights)
        
    #%% Evaluate method
    def Evaluate(self, mode):
        # Call functions to generate both world and robot(brain,body)
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        # Run the file
        if mode =="DIRECT":
            os.system("python3 simulate.py DIRECT")
        elif mode == "GUI":
            os.system("python3 simulate.py GUI")
        else:
            raise ValueError("Invalid mode. Use 'DIRECT' or 'GUI'.")
        
        # Read fitness value from fitness.txt
        with open("fitness.txt","r") as fitnessFile:
            fitness_string = fitnessFile.readline().strip()
            self.fitness = float(fitness_string)
        
        #Close fitness.txt
        fitnessFile.close()
        
        
        
    #%% Create World
    def Create_World(self):
        ## CREATE THE WORLD ##
        # Give pyrosim name of file that stores information about world
        pyrosim.Start_SDF("world.sdf")
        
        # End simulation
        pyrosim.End()
    
    #%% Create Body
    def Create_Body(self):
        ## CREATE THE ROBOT ##
        # Give pyrosim name of file to store information about robot
        pyrosim.Start_URDF("body.urdf")
        
        # Create a single link for torso
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1]) #Position and size of link
        
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5], size=[1,1,1]) #Position and size of link
      
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5], size=[1,1,1]) #Position and size of link
               
        # End Simulation
        pyrosim.End()
        
    #%% Create Brain
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")   
        
        # Neurons for loop
        self.sensor_neurons = ["Torso", "BackLeg", "FrontLeg"] #Sensor neurons
        self.motor_neurons = ["Torso_BackLeg","Torso_FrontLeg"] #Motor neurons
        
        # Iterate over each sensor neuron
        for currentRow in range(3):
            sensorIndex = currentRow   #Get index for sensor
            pyrosim.Send_Sensor_Neuron(name = sensorIndex, linkName = self.sensor_neurons[currentRow]) #Create sensor neuron with index and sensorname
            
            #Iterate over motor neurons
            for currentColumn in range(2):
                motorIndex =  int(currentColumn) + 3 #Get index of motor; +3 for 3 sensor neurons
                pyrosim.Send_Motor_Neuron(name = motorIndex, jointName = self.motor_neurons[currentColumn])
                
                #Assign weights
                self.weight = random.uniform(-1,1)
                pyrosim.Send_Synapse(sourceNeuronName = sensorIndex, targetNeuronName = currentColumn +3, weight = self.weights[currentRow][currentColumn])
      
        # End Simulation
        pyrosim.End()
        
    #%% Mutate!
    def Mutate(self):
        
        #Generate random integers to select random rows/columns
        randomRow = random.randint(0,2)
        randomColumn= random.randint(0,1)
        
        # Update random neuron with new, mutated weight
        self.weights[randomRow, randomColumn] = random.random() * 2 -1
        
        
        
        
        
        