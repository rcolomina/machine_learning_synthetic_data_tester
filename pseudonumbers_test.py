#!/usr/bin/python

from pseudonumbers import PseudoNumbers
import matplotlib.pyplot as plt

# Generate synthetic data
mynoise = PseudoNumbers()
mynoise.genSerie(10000)
Xtrain,Ytrain = mynoise.getTrainData()
Xtest,Ytest   = mynoise.getTestData()

# Plot synthetic data
gendata = mynoise.getData()
plt.plot(gendata)
plt.ylabel('PseudoNumbers')
plt.show()



