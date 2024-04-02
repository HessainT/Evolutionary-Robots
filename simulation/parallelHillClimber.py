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
import os

#%% Class definition
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        
        # Check and delete temporary files if they exist
        if os.path.exists("brain*.nndf"):
            os.system("rm brain*.nndf")

        if os.path.exists("fitness*.txt"):
            os.system("rm fitness*.txt")
        
        # Next ID for "waiting" parent
        self.nextAvailableID = 0
        
        # Create dictionary that stores parents
        self.parents = {}
        
        # Iterate over population size
        for i in range(c.populationSize):
            parent = SOLUTION(self.nextAvailableID)         #Create new random parent
            self.nextAvailableID += 1                       #Increment ID system
            
            self.parents[i] = parent                        #Store parent in the dictinoary
        

    #%% Evolve method
    def Evolve(self):
        
        #Evaluate parents
        self.Evaluate(self.parents)
        
        # Evolve x generations (look inside constants to change)
        for currentGeneration in range(c.numberOfGenerations):
            
            # Evolve for x generations
            self.Evolve_For_One_Generation()
        
    #%% Method to evolve one generation
    def Evolve_For_One_Generation(self):
        
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)    #Evaluate children
        self.Print()
        self.Select()                   #Compete parent vs child
        
    #%% Spawn child
    def Spawn(self):
        
        #Create a dictionary to store all the children
        self.children = {}
        
        #Iterate over each parent, creating a child for each
        for key in self.parents:
            
            #Create deep copy of self.parent and store as self.child
            self.child = copy.deepcopy(self.parents[key])
            
            #Assign unique ID to child
            self.child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1       #Increment ID counter
            
            #Add child to dictionary
            self.children[key] = self.child

        
    #%% Mutate child
    def Mutate(self):
        
        for key,child in self.children.items():
            self.child.Mutate()
    
    #%% Select child
    def Select(self):
        
        #Replace parent w/ child if latter performs better
        for key in self.parents:
            parent = self.parents[key]
            child = self.children[key]
            
            if child.fitness < parent.fitness:
                self.parents[key] = child
        
    #%% Print function
    def Print(self):
        
        print()
        #Print fitness of parents and their children
        for key in self.parents:        
            print("\n\nParent fitness: ", self.parents[key].fitness, " Child fitness: ", self.children[key].fitness,"\n")
        print()
        
        
    #%% Show best solution
    def Show_Best(self):
        
        #Initialize test to find fittest
        best_fitness = float('inf')
        best_solution = None
        
        for key in self.parents:
            if self.parents[key].fitness < best_fitness:
                best_fitness = self.parents[key].fitness
                best_solution = self.parents[key]
        
        if best_solution is not None:
            
            best_solution.Start_Simulation("GUI")
        
    #%% Evaluate method
    def Evaluate(self, solutions):
        #Start simulation for each parent
        for key in self.parents:
            solutions[key].Start_Simulation("DIRECT")
        
        #Iterate over each parent to print fitness
        for key in self.parents:
            solutions[key].Wait_For_Simulation_To_End()
            print("Solution", key, "fitness: ", self.parents[key].fitness)