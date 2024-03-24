#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:53:21 2024

For Random Search
"""
#%% Imports
import os

#%% Main code chunk

for i in range(5):
    os.system("python3 generate.py")    #Execute generate.py
    os.system("python3 simulate.py")    #Execute simulate.py
