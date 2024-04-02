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
import time
import constants as c

#%% Solution Class
class SOLUTION:
    def __init__(self, myID):
        
        #Assign ID number for use
        self.myID = myID
        
        #Create matix w/ random weights in range [0,1]
        self.random_weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        #print("Random weights (before scaling): ", self.random_weights)
        
        # Scale weights t orange [-1,1]
        self.weights = (self.random_weights * 2) -1
        #print("Random weights (after scaling): ", self.weights)
        
    #%% Start simulation
    def Start_Simulation(self,mode):
        # Call functions to generate both world and robot(brain,body)
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        # Run the file
        if mode =="DIRECT":
            #print("python3 simulate.py DIRECT & " + str(self.myID))
            os.system("python3 simulate.py DIRECT " + str(self.myID) + " 2&>1 &")
            #os.system("python3 simulate.py DIRECT &")
        elif mode == "GUI":
            #print("python3 simulate.py GUI & " + str(self.myID))
            os.system("python3 simulate.py GUI " + str(self.myID) + " 2&>1 &")
            #os.system("python3 simulate.py GUI &")
        else:
            raise ValueError("Invalid mode. Use 'DIRECT' or 'GUI'.")
            
    #%% Wait for simulation to end
    def Wait_For_Simulation_To_End(self):
        # Create string to feed into os.path
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        #Sleep for a bit if file doesn't exist
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
            
        # Read fitness value from fitness.txt        
        with open("fitness" + str(self.myID) + ".txt","r") as fitnessFile:
                        
            #Get fitness value from file
            fitness_string = fitnessFile.readline().strip()     #Strip line
            if fitness_string == '':
                self.fitness = 0
            else:
                self.fitness = float(fitness_string)                #Load in fitness into local variable
        
        #Close fitness.txt
        fitnessFile.close()
        
        #Delete file
        os.system("rm " + fitnessFileName)
        
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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1]) #Position and size of link
        
        #BackLeg Stuff
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2]) #Position and size of link
      
        #FrontLeg Stuff
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2]) #Position and size of link
        
        #LeftLeg Stuff
        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,0,0], size=[1,0.2,0.2]) #Position and size of link
        
        #RightLeg Stuff
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0], size=[1,0.2,0.2]) #Position and size of link
        
        pyrosim.Send_Joint(name = "BackLeg_BackLowLeg" , parent= "BackLeg" , child = "BackLowLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowLeg", pos=[0,0,-.5], size=[0.2,0.2,1]) #Position and size of link
        
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowLeg" , parent= "FrontLeg" , child = "FrontLowLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowLeg", pos=[0,0,-.5], size=[0.2,0.2,1]) #Position and size of link
        
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowLeg" , parent= "LeftLeg" , child = "LeftLowLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowLeg", pos=[0,0,-.5], size=[0.2,0.2,1]) #Position and size of link
        
        pyrosim.Send_Joint(name = "RightLeg_RightLowLeg" , parent= "RightLeg" , child = "RightLowLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowLeg", pos=[0,0,-.5], size=[0.2,0.2,1]) #Position and size of link
               
        # End Simulation
        pyrosim.End()
        
    #%% Create Brain
    def Create_Brain(self):
        #Create unique filename for each brain
        brain_id = "brain{}.nndf".format(self.myID)
        pyrosim.Start_NeuralNetwork(brain_id)   #Use unique filename to start neural network
        
        # Neurons for loop
        self.sensor_neurons = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg", 
                               "BackLowLeg", "FrontLowLeg", "LeftLowLeg", "RightLowLeg"] #Sensor neurons
        self.motor_neurons = ["Torso_BackLeg","Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", 
                              "BackLeg_BackLowLeg", "FrontLeg_FrontLowLeg", "LeftLeg_LeftLowLeg", "RightLeg_RightLowLeg"] #Motor neurons
                
        # # Neurons for loop
        # self.sensor_neurons = [ 
        #                        "BackLowLeg", "FrontLowLeg", "LeftLowLeg", "RightLowLeg"] #Sensor neurons
        # self.motor_neurons = [ 
        #                       "BackLeg_BackLowLeg", "FrontLeg_FrontLowLeg", "LeftLeg_LeftLowLeg", "RightLeg_RightLowLeg"] #Motor neurons
        
        # Iterate over each sensor neuron
        for currentRow in range(c.numSensorNeurons):
            sensorIndex = currentRow   #Get index for sensor
            pyrosim.Send_Sensor_Neuron(name = sensorIndex, linkName = self.sensor_neurons[currentRow]) #Create sensor neuron with index and sensorname
            # [currentRow+ 5] to only simulate feet sensors
            
            #Iterate over motor neurons
            for currentColumn in range(c.numMotorNeurons):
                motorIndex =  int(currentColumn) + c.numSensorNeurons  #Get index of motor; +3 for 3 sensor neurons
                pyrosim.Send_Motor_Neuron(name = motorIndex, jointName = self.motor_neurons[currentColumn])
                # [currentColumn + 4] to only simulate feet motors
                
                #Assign weights
                self.weight = random.uniform(-1,1)
                pyrosim.Send_Synapse(sourceNeuronName = sensorIndex, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
      
        # End Simulation
        pyrosim.End()

        
    #%% Mutate!
    def Mutate(self):
        
        #Generate random integers to select random rows/columns
        randomRow = random.randint(0,c.numSensorNeurons -1)
        randomColumn= random.randint(0,c.numMotorNeurons -1)
        
        # Update random neuron with new, mutated weight
        self.weights[randomRow, randomColumn] = random.random() * 2 -1
        
    #%% Set new ID method
    def Set_ID(self, myID):
        # Assign argument ID to local space
        self.myID = myID
        
        
        
        