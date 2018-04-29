#!/usr/bin/python
import random
import math

from common.datagenerator import DataGenerator
from interface import implements

class SinNoise(DataGenerator):
    def __init__(self,amp,freq,trans=0.0,noise=0.0,
                 sizeX=20,foreY=5,train_percent=0.7,
                 seriesize=1000):
        
        # Variables to store the model
        self.amp    = amp
        self.freq   = freq
        self.trans  = trans
        self.noise  = noise        
        self.counter= 0
        self.deltaTime = 0.01
        
        # sizeX and foreY must be integers
        self.sizeX  = sizeX
        self.foreY  = foreY
        self.train_percent = train_percent
        
    # Data origin on each iteration using counter
    def model(self):
        # Use counter to get the following data        
        time         = self.counter * self.deltaTime
        pi           = math
        angularFreq  = 2.0 * math.pi * self.freq
        phase        = 0.0
        arg1         = angularFreq * time + phase
        arg2         = angularFreq * time + 2 * phase
        determinism  = self.amp * math.sin(arg1) + self.amp * math.cos(arg2) + time * 100.0
        randomsample = random.random() -  0.5
        randomnoise  = self.noise * randomsample
        #print determinism
        calmodel     = randomnoise + determinism + self.trans
        return calmodel
            

    def printParams(self):
        print "Amp:  ",self.amp
        print "Freq: ",self.freq
        print "Tran: ",self.trans
        print "Noise:",self.noise
        print "Counter:",self.counter
        
                    
    def writeData(self):
        print "TODO"

