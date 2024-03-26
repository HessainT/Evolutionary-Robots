#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:30:04 2024

@author: hessain
"""
#%% For Joints
# Import packages
import pyrosim.pyrosim as pyrosim
import random

#%% Generate the body
def Generate_Body():
    
    ## CREATE THE WORLD ##
    # Give pyrosim name of file that stores information about world
    pyrosim.Start_SDF("world.sdf")
    
    # End simulation
    pyrosim.End()


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

#%% Generate the Brain
def Generate_Brain():

    pyrosim.Start_NeuralNetwork("brain.nndf")   
    
    # Neurons for loop
    sensor_neurons = ["Torso", "BackLeg", "FrontLeg"] #Sensor neurons
    motor_neurons = ["Torso_BackLeg","Torso_FrontLeg"] #Motor neurons
    
    # Iterate over each sensor neuron
    for sensorName in sensor_neurons:
        sensorIndex = sensor_neurons.index(sensorName) #Get the index of the sensor
        pyrosim.Send_Sensor_Neuron(name = sensorIndex, linkName = sensorName) #Create sensor neuron with index and sensorname
        
        #Iterate over motor neurons
        for motorName in motor_neurons:
            motorIndex = motor_neurons.index(motorName) + 3 #Get index of sensor; +3 because 3 sensor neurons in outer loop
            pyrosim.Send_Motor_Neuron(name = motorIndex, jointName = motorName)
            
            #Assign weights
            weight = random.uniform(-1,1)
            pyrosim.Send_Synapse(sourceNeuronName = sensorIndex, targetNeuronName = motorIndex, weight = weight)
        
       
    # #Send sensor neurons
    # pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")   
    # pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
    # pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
    
    # pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
    # pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")
    
    
    # #Generate a synapse
    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = .5) 
    # #Idk why but weight has to be -1 here, otherwise the robot breaks. :'(
    # pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = .5)
    # pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = .5)
    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = .5)
    # pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = .5)
    # pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = .5)
    
    
    # End Simulation
    pyrosim.End()

#%% Use the functions
Generate_Body()
Generate_Brain()



#%% Generate the 5x5 block world
# # Import packages
# import pyrosim.pyrosim as pyrosim

# # Set how tall block tower is going to be
# block_height = 10

 
# #Set x,y,z coordinates for first block
# x = 0 # Depth ("Depth" going left)
# y = 0   # Length
# z = .5  #Height


# # Give pyrosim name of file that will store information about world
# pyrosim.Start_SDF("boxes.sdf")

# # Set rows 
# rows = 5
# for i in range(rows): # Loop through to get rows
    
#     x = 0
#     z = .5
#     # Set columns
#     columns = 5
#     for i in range(columns): # Loop through to get columns
#         # Set sizes for blocks
#         size = 1
        
#         # Loop will iterate and create enough blocks for tower
#         for i in range(block_height):
                      
#             # Create links (boxes)
#             pyrosim.Send_Cube(name = f"Box_{i}", pos =[x,y,z] , size = [size,size,size]) # Size is (Depth, Length, Height)
#             # pyrosim.Send_Cube(name = "Box2", pos =[x+1,y,z+1] , size = [1,1,1]) # Size is (Depth, Length, Height)
            
#             # Adjust position of consecutive block
#             z += 1
            
#             # Adjust size of consecutive block
#             size *= .9
        
#         x += 1
#         z -= 10
        
#     y += 1
#     z -= 10

# pyrosim.End()
