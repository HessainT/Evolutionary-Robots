#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:53:21 2024

"""
#%% Imports
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#%% Main code chunk
phc = PARALLEL_HILL_CLIMBER()     #Create a Hill Climber object
phc.Evolve()        #Call evolve function from hillclimber

#print("Showing best now")
phc.Show_Best()      #Show the best from generation


# for i in range(5):
#     os.system("python3 generate.py")    #Execute generate.py
#     os.system("python3 simulate.py")    #Execute simulate.py
