import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)

    def Add_To_Value( self, value ):
        
        #Convert value to float
        #value = float(value)

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):
        
        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        self.Print_Value()

        # print("")

    def Set_Value(self,value):

        self.value = value

# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)
        
    #Hessain Addition
    def Update_Sensor_Neuron(self):
        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()))
        
    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):
        
        #Set value to 0
        self.Set_Value(0)

        #Initialize value to 0 for loop
        self.init_neuron_value = 0
        
        #TESTING
        # #Print current key in synapse?
        # print(self.Get_Name())
        # print("\n updating neuron")
        
        print("Value before synapse")
        print(self.Get_Value())
        
        # Iterate through keys in synapse
        for key in synapses:
            
            # Check whether current synapse arrives at correct neuron
            if (key[1] == self.Get_Name()):
                    
                # Testing
                # print(key[0])
                # print(key[1])
                # print("pre and post synapse neurons")
                
                # Get the presynaptic neuron's name and weight of the synapse
                self.pre_neuron_name = key[0]                        #Name of neuron
                self.synapse_weight = synapses[key].Get_Weight()     #Weight of neuron
    
                # Get the current value of the presynaptic neuron
                self.pre_neuron_value = neurons[self.pre_neuron_name].Get_Value()
                
                # Call Allow_Presynaptic_Neuron_To_Influence_Me method
                self.Allow_Presynaptic_Neuron_To_Influence_Me(self.synapse_weight, self.pre_neuron_value)
        
        # Sets motor max output to [-1.0,1.0]
        self.Threshold()
        print("Value after synapse")
        print(self.Get_Value())
        
    def Allow_Presynaptic_Neuron_To_Influence_Me(self, weight, value):
        
        # Print arguments to test
        print(weight)
        print("weight")
        print(value)
        print("value)")
        
        #Calculate outgoing signal and send it out
        self.output = weight * value
        
        #self.output = float(self.output)    #Convert value to float
        self.Add_To_Value(self.output)        
