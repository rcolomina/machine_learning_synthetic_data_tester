#!/usr/bin/python
from sklearn import linear_model

from common.datapredictor import Predictor
from interface import implements

class BayesRidgePredict(implements(Predictor)):    
    def __init__(self):
        self.trained = False
        self.model = linear_model.BayesianRidge()
        self.samplestrained = 0
        
    def predict(self,sample):
        if not self.trained:
            print "Model not trained"
            return False
        return self.model.predict(sample)
    
    def train(self,Xtrain,Ytrain):
        # fit the model with training data
        self.model.fit(Xtrain,Ytrain)
        self.samplestrained = len(Xtrain)
        self.trained = True
        print "Model trained"
        return True
        
    # Get score on test data
    def score(self,Xtest,Ytest):
        # check (Xtest, Ytest) are different from (Xtrain,Ytrain)
        return self.model.score(Xtest,Ytest)

    #Partialy train
    def update(self,Xup,Yup):
        self.trained = True
        self.sampestrained += len(Xup)
        self.model.partial_fit(Xup,Yup)
        
        
