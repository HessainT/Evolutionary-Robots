#%% Import everything
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import random
import constants as c
from simulation import SIMULATION
from world import WORLD
from robot import ROBOT
import sys

#%% Initialize instances of classes with empty constructors

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI) 
simulation.Run()
simulation.Get_Fitness()

