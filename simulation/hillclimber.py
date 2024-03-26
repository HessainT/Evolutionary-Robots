#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:07:28 2024

@author: hessain
"""

#%% Imports
from solution import SOLUTION
import constants as c
import copy

#%% Class definition
class HILL_CLIMBER:
    def __init__(self):
        # Create solution
        self.parent = SOLUTION()
        

    #%% Evolve method
    def Evolve(self):
        
        #Evaluate the parent
        self.parent.Evaluate("GUI")
        
        # Evolve x generations (look inside constants to change)
        for currentGeneration in range(c.numberOfGenerations):
            
            # Evolve for x generations
            self.Evolve_For_One_Generation()
        
    #%% Method to evolve one generation
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
        
    #%% Spawn child
    def Spawn(self):
        
        #Create deep copy of self.parent and store as self.child
        self.child = copy.deepcopy(self.parent)
        
    #%% Mutate child
    def Mutate(self):
        
        #Call mutate method
        self.child.Mutate()
        
        # # Check weights of parent and child
        # print("Parent weights: ")
        # print(self.parent.weights)
        # print("CHild weights: ")
        # print(self.child.weights)
        
        # exit()
    
    #%% Select child
    def Select(self):
                
        #Replace parent w/ child if latter performs better
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
        
    #%% Print function
    def Print(self):
        #Print fitness of parent and child
        print("\n\nParent fitness: ", self.parent.fitness, " Child fitness: ", self.child.fitness,"\n")
        
        
    #%% Show best solution
    def Show_Best(self):
        self.parent.Evaluate("GUI")