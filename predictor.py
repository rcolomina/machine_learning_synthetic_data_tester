#!/usr/bin/python
from gensinnoise import SinNoise
from sklearn import linear_model
import sys

# Training Data
mynoise = SinNoise(amp=100.0,freq=0.1,noise=0.5,sizeX=50,foreY=5)
mynoise.genSerie(10000)
X,Y = mynoise.getXYData()

# Test Data
mynoise.reset()
mynoise.genSerie(1000)
Xtest,Ytest = mynoise.getXYData()

# Model
myModel = linear_model.BayesianRidge()

# fit the model with training data
myModel.fit(X,Y)

# Score the model using training data
print "Score on the model:",myModel.score(Xtest,Ytest)

# Predict some value
for i in range(0,20):    
    print "Predictions on Xtest(",i,"):",myModel.predict(Xtest[i])," vs Ytest[",i,"]:",Ytest[i]

print X[0]
print Y[0]
