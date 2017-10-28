#!/usr/bin/python
#from gensinnoise   import SinNoise
from pseudonumbers import PseudoNumbers
from bayesridgepredictor import BayesRidgePredict
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# Select Data generatior model
genmodel = 1
# Select Data predictor model
premodel = 0

# Generate Data Model 
if genmodel ==0:
    mynoise = SinNoise(amp=100.0,
                       freq=20.0,
                       noise=0.1,
                       foreY=20)
else:
    if genmodel == 1:
        mynoise = PseudoNumbers()
    else:
        print "Erro: Model not considered"
        sys.exit()
    
# Generate Syinthetic Data
mynoise.genSerie(50000)
Xtrain,Ytrain = mynoise.getTrainData()
Xtest,Ytest   = mynoise.getTestData()


# Create the model predictor
if premodel == 0:
    myBRP = BayesRidgePredict()
else:
    print "Error: Model not considered"
    sys.exit()
    
#myBRP.train(Xtrain,Ytrain)
#print "Predicted:",myBRP.predict(Xtest[0])," - Actual:",Ytest[0]
#print myBRP.score(Xtrain,Ytrain)

online=False
batch=True
# LEARNING ONLINE
if online:
    counter = 10
    Xup = Xtrain[0:counter]
    Yup = Ytrain[0:counter]
    myBRP.train(Xup,Yup)

    counter += 1
    while True:
        Xup = Xtrain[0:counter]
        Yup = Ytrain[0:counter]
        myBRP.train(Xup,Yup)

        ErrorPrediction = myBRP.predict(Xtrain[counter]) - Ytrain[counter]
        #    print "Counter",mynoise.counter,"Prediction:",myBRP.predict(Xtrain[counter+1])," Actual:",Ytrain[counter+1]#," Score:",myBRP.score(Xup,Yup)
        print "Error Prediction:",ErrorPrediction #," Score:",myBRP.score(Xtest,Ytest) 
        counter +=1
        #print "Current Score:",myBRP.score(Xtest,Ytest)
        time.sleep(0.1)


# BACTH LEARNING
if batch:
    myBRP.train(Xtrain,Ytrain)        

    print "Score:",myBRP.score(Xtest,Ytest)
    errors = []
    for i in range(0,len(Xtest)):
        errors.append(myBRP.predict(Xtest[i])-Ytest[i])
        
    #print "Predicted:",myBRP.predict(Xtest[0])," - Actual:",Ytest[0]    
    print "Max Error:",max(errors)
    print "Std Error:",np.std(errors)

    # the histogram of the data
    #n, bins, patches = plt.hist(errors,50,normed=1, facecolor='g', alpha=0.75)

    #plt.xlabel('Errors')
    #plt.ylabel('Probability')
    #plt.title('Histogram of Errors')
    #plt.axis([-50,50, 0, 0.1])
    #plt.grid(True)
    #plt.show()

    #print errors[0:100]
    plt.plot(errors[0:1000])
    plt.ylabel('Errors')
    plt.show()

    
