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

#%% Initialize instances of classes with empty constructors
simulation = SIMULATION() 
simulation.Run()


#%% Old Code
 # # Create an object to handle and draw results to GUI
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# # OPTIONAL: Disable sidebars
# #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# # Import world
# # Adjust simulation world
# p.setGravity(c.grav_x, c.grav_y, c.grav_z) # Set gravity to Earth value

# planeId = p.loadURDF("plane.urdf")  # Read in the plane
# robotId = p.loadURDF("body.urdf")   # Read in the robot

# # Load  the simulation
# p.loadSDF("world.sdf")

# # Set up before stepping simulation
# STEPS = c.STEPS #How many Steps to take
# pyrosim.Prepare_To_Simulate(robotId) #Set up sensor

# # Create arrays to save sensor values to
# backLegSensorValues = np.zeros(STEPS) #Create numpy array with same length as steps
# frontLegSensorValues = np.zeros(STEPS)

# #%% # Back Leg Open-loop control using sin
# bleg_time_values = np.linspace(c.lower_time_bound, c.upper_time_bound, STEPS) #Create array for range of values and subdivisions (STEPS)

# bleg_amplitude = c.back_amplitude     #Amplitude multiplier
# bleg_frequency = c.back_frequency     #Frequency multiplier
# bleg_phase_offset = c.back_phase      #Set phase offset

# bleg_target_angles = bleg_amplitude * np.sin(bleg_frequency * bleg_time_values) + bleg_phase_offset #Create the sin function

# # Save function
# np.save("data/bleg_targetAngles.npy", bleg_target_angles)

# #%% # Front Leg Open-loop control using sin
# fleg_time_values = np.linspace(c.lower_time_bound, c.upper_time_bound, STEPS) #Create array for range of values and subdivisions (STEPS)

# fleg_amplitude = c.front_amplitude     #Amplitude multiplier
# fleg_frequency = c.front_frequency     #Frequency multiplier
# fleg_phase_offset = c.front_phase     #Set phase offset

# fleg_target_angles = fleg_amplitude * np.sin(fleg_frequency * fleg_time_values) + fleg_phase_offset #Create the sin function

# # Save function
# np.save("data/fleg_targetAngles.npy", fleg_target_angles)

# #%% Looping through action
# # Loop through the action
# for i in range(STEPS): 
#     p.stepSimulation() # Step
    
#     # Collect touch sensor values at current step
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
#     # Backleg motor
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = "Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = bleg_target_angles[i],
#         maxForce = c.max_force)
        
    
#     # Frontleg motor
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = "Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = fleg_target_angles[i],
#         maxForce = c.max_force)
    
#     time.sleep(c.sleep_duration) # Sleep for 1/60 second

# p.disconnect #Disconnect object

# # Save values in sensors into file
# np.save("data/backLegReadings.npy", backLegSensorValues)
# np.save("data/frontLegReadings.npy", frontLegSensorValues)


# print(backLegSensorValues) #Print sensor value
