#!/usr/bin/python
from interface import Interface

class DataGenerator(Interface):
    
    def model(self):
        pass
    def genSerie(self,seriesize):
        pass
    def getData(self):
        pass
    def printParams(self):
        pass
    def writeData(self):
        pass
    
    # common implementation
    def gen(self):
        register = self.model()
        self.counter += 1
        return register
    def reset(self):
        counter = 0
        self.data = []

    

    
