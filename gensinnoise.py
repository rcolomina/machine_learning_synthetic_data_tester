#!/usr/bin/python
import random
import math

from datagenerator import DataGenerator
from interface import implements

class SinNoise(implements(DataGenerator)):
    def __init__(self,amp,freq,trans=0.0,noise=0.0,
                 sizeX=20,foreY=5,train_percent=0.7,
                 seriesize=1000):
        
        self.data = []
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
        
        self.X = []
        self.Y = []
        
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
            
    def genSerie(self,seriesize):
        serie = []
        for i in range(0,seriesize):
            newData = self.gen()
            self.data.append(newData)
            serie.append(newData)
        
        # Create X,Y arrays
        self.X,self.Y = self.getXYData()
    
    def getData(self):
        return self.data

    def printParams(self):
        print "Amp:  ",self.amp
        print "Freq: ",self.freq
        print "Tran: ",self.trans
        print "Noise:",self.noise
        print "Counter:",self.counter
        
    def getXYData(self):
        xDim = self.sizeX
        yfd  = self.foreY

        if xDim < 1 or yfd < 1:
            return -1

        imax = len(self.data)-xDim-yfd+1
        
        #print len(self.data)
        X = [self.data[i:i+xDim] for i in xrange(0,imax)]
        Y = [self.data[i+xDim+yfd-1] for i in range(0,imax)]
    
        return X,Y
                    
    def writeData(self):
        print "TODO"

    def getTrainData(self):
        if self.X == []:
            return -1
        X = self.X
        Y = self.Y
        
        trainsize = int(len(X) * self.train_percent)
        Xtrain = X[0:trainsize]
        Ytrain = Y[0:trainsize]
        return Xtrain,Ytrain
        
        
    def getTestData(self):
        if self.X == []:
            return -1
        X = self.X
        Y = self.Y

        trainsize = int(len(X) * self.train_percent)
        Xtest = X[trainsize:len(X)]
        Ytest = Y[trainsize:len(X)]

        return Xtest,Ytest
