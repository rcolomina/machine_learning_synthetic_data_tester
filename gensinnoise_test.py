#!/usr/bin/python
from gensinnoise import SinNoise

mynoise = SinNoise(10.0,0.5,0.0,0.1)

mynoise.genSerie(30)
X,Y = mynoise.getXYData()

#print "DATA:",mynoise.getData()
#print "X",X
print "len(X):",len(X)
#print "Y",Y
print "Y:",len(Y)
