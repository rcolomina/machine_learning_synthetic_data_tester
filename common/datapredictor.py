#!/usr/bin/python
#from interface import Interface

class Predictor(object):

    def __init__(self):
        self.model = None
        self.samplestrained = 0
        self.trained = False
            
    # Return a prediction using a sample
    def predict(self,sample):
        pass
    
    # Train the model underneath the predictor
    def train(self,Xtrain,Ytrain):
        if self.model != None:
            # fit the model with training data
            self.model.fit(Xtrain,Ytrain)
            self.samplestrained = len(Xtrain)
            self.trained = True
            print "Model trained"
            return True
        return False
        
