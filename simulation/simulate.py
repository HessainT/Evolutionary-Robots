# Import stuff
import pybullet as p
import time

# Create an object to handle and draw results to GUI
physicsClient = p.connect(p.GUI)

# OPTIONAL: Disable sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# Stepping the simulation
# Loop through the action
for i in range(1000): 
    p.stepSimulation() # Step
    time.sleep(1/60) # Sleep for 1/60 second
    print(i)

p.disconnect #Disconnect object


