#!/usr/bin/python
import random
import math

from common.datagenerator import DataGenerator

class PseudoNumbers(DataGenerator):
    def __init__(self,
                 noise=0.01,
                 sizeX=20,foreY=5,
                 train_percent=0.7,
                 seriesize=10000):

        self.noise  = noise
        self.counter= 0
        self.deltaTime = 0.01
        # sizeX and foreY must be integers
        self.sizeX  = sizeX
        self.foreY  = foreY
        self.train_percent = train_percent
        
        self.event0 = 100
        self.event1 = 200
        self.event2 = 300
        self.calmodel = 0

    # Return what the model has defined
    def model(self):
        # Use counter to get the following data        
        if self.counter % 50: 
            self.calmodel += 5

        if self.counter > 500:
            self.counter = 0

        randomsample = random.random() -  0.5
        return self.calmodel + self.counter + randomsample * self.noise
                
    def printParams(self):
        print "Noise:",self.noise
        print "Counter:",self.counter
                            
    def writeData(self):
        print "TODO"

        
