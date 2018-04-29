#!/usr/bin/python

# Time series data generator
class DataGenerator(object):

    # Inicialize common data
    def __init__(self):
        self.data = [] # all data
        self.X = []    # features
        self.Y = []    # labels
        self.counter = 0  # Samples generated
        self.train_percent = 0.5 # Spliting train and test
        self.sizeX = 0
        self.foreY = 0
        
    # PRIVATE METHODS
    def _checkData(self,trainpercent):
        if self.X == []:
            return False        
        X = self.X
        Y = self.Y    
        trainsize = int(len(X) * self.train_percent)
        return X,Y,trainsize

    # common implementation
    def _gen(self):
        register = self.model()
        self.counter += 1
        return register
    
    # Method to overwrite by derived classes
    def model(self):
        raise NotImplementedError()    

    def genSerie(self,seriesize=100):
        self.data = [self._gen() for i in xrange(0,seriesize)]
        self.X,self.Y = self.getXYData()
        return True
    
    def reset(self):
        counter = 0
        self.data = []
        return None
        
    def getData(self):
        return self.data
    
    def getTrainData(self):
        X,Y,trainsize = self._checkData(self.train_percent)
        Xtrain = X[0:trainsize]
        Ytrain = Y[0:trainsize]
        return Xtrain,Ytrain        

    def getTestData(self):
        X,Y,trainsize = self._checkData(self.train_percent)        
        Xtest = X[trainsize:len(X)]
        Ytest = Y[trainsize:len(X)]    
        return Xtest,Ytest

    # Split Data in features and labels
    def getXYData(self):
        sizeCondOnXYdata = self.sizeX < 1 or self.foreY < 1
        if sizeCondOnXYdata:
            return False

        # Calculate imax
        xDim = self.sizeX
        yfd  = self.foreY    
        imax = len(self.data)-xDim-yfd+1
        
        # Split time series in features and labels
        X = [self.data[i:i+xDim] for i in xrange(0,imax)]
        Y = [self.data[i+xDim+yfd-1] for i in xrange(0,imax)]
    
        # Return data in shape of X,Y
        return X,Y

