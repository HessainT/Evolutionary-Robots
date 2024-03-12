#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:14:18 2024

@author: hessain
"""

#%% Import Stuff
import numpy as np
import matplotlib.pyplot as plt

#%% Sensor Stuff
# Load Sensor values
backLegSensorValues = np.load("data/backLegReadings.npy")
frontLegSensorValues = np.load("data/frontLegReadings.npy")
#print(backLegSensorValues) #Print to test

# Plot data
plt.plot(backLegSensorValues, label= "Back Leg", linewidth = "2") #Plot back leg data
plt.plot(frontLegSensorValues, label= "Front Leg", linewidth = "1")  #Plot front leg data
plt.legend() #Include legend
plt.show() #Show plot

#%% Back Leg Motor stuff
# Load target angles
target_angles = np.load("data/bleg_targetAngles.npy")

# Plot
plt.plot(target_angles, label= "Back Leg Target angles")
plt.title("Motor Commands")
plt.xlabel("Steps")
plt.ylabel("Vale in Radians")
plt.legend()
plt.show()

#%% Front LegMotor stuff
# Load target angles
target_angles = np.load("data/fleg_targetAngles.npy")

# Plot
plt.plot(target_angles, label= "Front Leg Target angles")
plt.title("Motor Commands")
plt.xlabel("Steps")
plt.ylabel("Vale in Radians")
plt.legend()
plt.show()