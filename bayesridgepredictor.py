#!/usr/bin/python
from sklearn import linear_model

from common.datapredictor import Predictor
#from interface import implements

class BayesRidgePredict(Predictor):    
    def __init__(self):
        self.trained = False
        self.model = linear_model.BayesianRidge()
        self.samplestrained = 0
        
    def predict(self,sample):
        if not self.trained:
            print "Model not trained"
            return False
        try:
            ret_model = self.model.predict(sample)
            return ret_model
        except ValueError:
            print "Model could not predict ",ValueError
    
        
    # Get score on test data
    def score(self,Xtest,Ytest):
        # check (Xtest, Ytest) are different from (Xtrain,Ytrain)
        return self.model.score(Xtest,Ytest)

    #Partialy train
    def update(self,Xup,Yup):
        self.trained = True
        self.sampestrained += len(Xup)
        self.model.partial_fit(Xup,Yup)
        
        
