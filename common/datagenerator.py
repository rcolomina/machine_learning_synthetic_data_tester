#!/usr/bin/python

class DataGenerator(object):
    def model(self):
        raise NotImplementedError()    
    def genSerie(self,seriesize):
        raise NotImplementedError()

#    def printParams(self):
#        pass
#    def writeData(self):
#        pass
    
    # common implementation
    def gen(self):
        register = self.model()
        self.counter += 1
        return register
    
    def reset(self):
        counter = 0
        self.data = []
        
    def getData(self):
        return self.data

    def getTrainData(self):
        if self.X == []:
            return False
        
        X = self.X
        Y = self.Y
        
        trainsize = int(len(X) * self.train_percent)
        Xtrain = X[0:trainsize]
        Ytrain = Y[0:trainsize]
        return Xtrain,Ytrain        

    def getTestData(self):
        if self.X == []:
            return False
        X = self.X
        Y = self.Y

        trainsize = int(len(X) * self.train_percent)
        Xtest = X[trainsize:len(X)]
        Ytest = Y[trainsize:len(X)]

        return Xtest,Ytest

    

    
