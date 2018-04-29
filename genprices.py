#!/usr/bin/python
import random
import math

from common.datagenerator import DataGenerator

class BTCPriceGenerator(DataGenerator):

    def __init__(self,
                 filename,
                 sizeX=20,
                 foreY=5,
                 train_percent=0.7,                 
                 seriesize=100):

        # trained data
        self.data = []

        # sizeX and foreY must be integers
        self.sizeX  = sizeX
        self.foreY  = foreY
        self.train_percent = train_percent

        # features and labels
        self.X = []
        self.Y = []
        self.dataFile = []
        self.counter = 0
 #       self.readfile(filename)
        
 #'   def readFile(self,filename):
        # open file and read into memory
        f = open(filename,'r')
        for line in f:
            self.dataFile.append(line)

        f.close()
                
    def model(self):
        #print len(self.dataFile)
        fileRegister = self.dataFile[self.counter]
        choppedReg = fileRegister.split(' ')

        askprice = choppedReg[4]
        bidprice = choppedReg[13]
        middleprice = (float(askprice)+float(bidprice))/2.0
        #print "ask",askprice
        #print "bidprice",bidprice
        print  middleprice 
        return middleprice 


        
