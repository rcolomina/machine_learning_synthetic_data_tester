#!/usr/bin/python
from genprices import BTCPriceGenerator

myprices = BTCPriceGenerator("prices.dat",seriesize=10)

myprices.genSerie(10)


