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
        
        self.data = []
        self.noise  = noise
        self.counter= 0
        self.deltaTime = 0.01
        # sizeX and foreY must be integers
        self.sizeX  = sizeX
        self.foreY  = foreY
        self.train_percent = train_percent
        
        self.X = []
        self.Y = []

        self.event0 = 100
        self.event1 = 200
        self.event2 = 300
        self.calmodel = 0
        
    def model(self):
        # Use counter to get the following data        
        if self.counter % 50: 
            self.calmodel += 5

        if self.counter > 500:
            self.counter = 0

        randomsample = random.random() -  0.5
        return self.calmodel + self.counter + randomsample * self.noise
        
#    def gen(self):
#        register = self.model()
#        self.counter += 1
#        return register

#    def reset(self):
#        self.counter = 0
#        self.data = []
    
    def genSerie(self,seriesize):
        serie = []
        for i in range(0,seriesize):
            newData = self.gen()
            self.data.append(newData)
            serie.append(newData)
        
        # Create X,Y arrays
        self.X,self.Y = self.getXYData()
    
    def printParams(self):
        print "Noise:",self.noise
        print "Counter:",self.counter
        
    def getXYData(self):
        xDim = self.sizeX
        yfd  = self.foreY
        if xDim < 1 or yfd < 1:
            return False
        imax = len(self.data)-xDim-yfd+1        
       #print len(self.data)
        X = [self.data[i:i+xDim] for i in xrange(0,imax)]
        Y = [self.data[i+xDim+yfd-1] for i in range(0,imax)]
        return X,Y
                    
    def writeData(self):
        print "TODO"

        
