#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:53:21 2024

For Random Search
"""
#%% Imports
import os
from hillclimber import HILL_CLIMBER

#%% Main code chunk
hc = HILL_CLIMBER()     #Create a Hill Climber object
hc.Evolve()        #Call evolve function from hillclimber
print("Showing best now")
hc.Show_Best()      #Show the best from generation




# for i in range(5):
#     os.system("python3 generate.py")    #Execute generate.py
#     os.system("python3 simulate.py")    #Execute simulate.py
