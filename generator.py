import random
import time
import math

mem_param1 = 10.0 * random.random()-5.0
mem_param2 = 10.0 * random.random()-5.0
mem_param3 = 10.0 * random.random()-5.0 


def online_predictor(prev1,prev2,prev3):
    #My model
    prediction = mem_param1 * prev1 + \
                 mem_param2 * prev2 + \
                 mem_param3 * prev3 + \
                 mem_param1 * prev1 * prev1+ \
                 mem_param2 * prev2 * prev2+ \
                 mem_param3 * prev3 * prev3
    
    return prediction
    
def online_corrector(predicted_value,actual_value):
    prediction_error = actual_value - predicted_value
    print "Error                          ",prediction_error

    global mem_param1
    global mem_param2
    global mem_param3
    
    if prediction_error > 0:
        mem_param1 -= random.random() * 0.1
        mem_param2 -= random.random() * 0.1
        mem_param3 -= random.random() * 0.1
    else:
        mem_param1 += random.random() * 0.1
        mem_param2 += random.random() * 0.1
        mem_param3 += random.random() * 0.1

    print "New Model:",mem_param1," ",mem_param2," ",mem_param3

    return prediction_error

    
oldvals=[0,0,0]

counter=0
while True:
    print "==================================="
    
    time.sleep(0.5)
    counter+=1
    divsor=10.0

    # Generate random and deterministic
    myrandom = random.random()
    mydeterm = math.sin(counter/10.0)

    # Do my prediction with oll value
    myprediction = online_predictor(oldvals[-1],oldvals[-2],oldvals[-3])    
    print "My prediction:               ",myprediction

    # Calculate new value for the time serie
    mytimeserie = myrandom+10*mydeterm
    print "My pseudo-random time series:",mytimeserie

    # Store old value
    oldvals.append(mytimeserie)

    # Correct model
    online_corrector(myprediction,mytimeserie)
