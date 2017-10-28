#!/usr/bin/python
#from interface import Interface

class Predictor(object):
    # Return a prediction using a sample
    def predict(self,sample):
        pass
    # Train the model underneath the predictor
    #def train(self,Xtrain,Ytrain):
    #    pass

    def train(self,Xtrain,Ytrain):
        # fit the model with training data
        self.model.fit(Xtrain,Ytrain)
        self.samplestrained = len(Xtrain)
        self.trained = True
        print "Model trained"
        return True

    # Test the model scoring on test data
    def score(self,Xtest,Ytest):
        pass
    # Update the model with new data
#    def update(self,X,Y):
#        pass
        
