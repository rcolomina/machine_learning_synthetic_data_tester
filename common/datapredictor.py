#!/usr/bin/python
from interface import Interface

class Predictor(Interface):
    # Return a prediction using a sample
    def predict(self,sample):
        pass
    # Train the model underneath the predictor
    def train(self,Xtrain,Ytrain):
        pass
    # Test the model scoring on test data
    def score(self,Xtest,Ytest):
        pass
    # Update the model with new data
#    def update(self,X,Y):
#        pass
        
