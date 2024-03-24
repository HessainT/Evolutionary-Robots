from pyrosim.neuron  import NEURON

from pyrosim.synapse import SYNAPSE

import sys

class NEURAL_NETWORK: 

    def __init__(self,nndfFileName):

        self.neurons = {}

        self.synapses = {}

        f = open(nndfFileName,"r")

        for line in f.readlines():

            self.Digest(line)

        f.close()

    def Print(self):

        self.Print_Sensor_Neuron_Values()

        self.Print_Hidden_Neuron_Values()

        self.Print_Motor_Neuron_Values()

        print("")
    
    #Added by Hessain
    def Update(self):
        
        for key in self.neurons:
            if self.neurons[key].Is_Sensor_Neuron():
                self.neurons[key].Update_Sensor_Neuron()
            else:
                self.neurons[key].Update_Hidden_Or_Motor_Neuron(self.neurons, self.synapses)
# ---------------- Private methods --------------------------------------

    def Add_Neuron_According_To(self,line):

        neuron = NEURON(line)

        self.neurons[ neuron.Get_Name() ] = neuron

    def Add_Synapse_According_To(self,line):

        synapse = SYNAPSE(line)

        sourceNeuronName = synapse.Get_Source_Neuron_Name()

        targetNeuronName = synapse.Get_Target_Neuron_Name()

        self.synapses[sourceNeuronName , targetNeuronName] = synapse

    def Digest(self,line):

        if self.Line_Contains_Neuron_Definition(line):

            self.Add_Neuron_According_To(line)

        if self.Line_Contains_Synapse_Definition(line):

            self.Add_Synapse_According_To(line)

    def Line_Contains_Neuron_Definition(self,line):

        return "neuron" in line

    def Line_Contains_Synapse_Definition(self,line):

        return "synapse" in line

    def Print_Sensor_Neuron_Values(self):

        print("sensor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Sensor_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Hidden_Neuron_Values(self):

        print("hidden neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Hidden_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Motor_Neuron_Values(self):

        print("motor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Motor_Neuron():

                self.neurons[neuronName].Print()

        print("")
    
    #Hessain addition
    def Get_Neuron_Names(self):
        
        #Return key of the neuron dictinoary (aka. neuron name)
        return self.neurons.keys()
    
    def Is_Motor_Neuron(self, neuronName):
        #Check if neuron is "registered"
        if neuronName in self.neurons:
            #Check in neuron.py whether neuron is motor neuron
            return self.neurons[neuronName].Is_Motor_Neuron()
        return False
    
    def Get_Motor_Neurons_Joint(self, neuronName):
        #Check if neuron is "registered"
        if neuronName in self.neurons:
            #Check in neuron.py whether neuron is motor neuron
            return self.neurons[neuronName].Get_Joint_Name()
        return 0
    
    def Get_Value_Of(self, neuronName):
        #Check if neuron is "registered"
        if neuronName in self.neurons:
            #Check in neuron.py whether neuron is motor neuron
            return self.neurons[neuronName].Get_Value()
        return 0
