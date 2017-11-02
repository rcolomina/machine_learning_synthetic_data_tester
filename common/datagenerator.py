#!/usr/bin/python
class DataGenerator(object):
    def model(self):
        raise NotImplementedError()    
    
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

