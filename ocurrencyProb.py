# Lab 02 Criptografía
# Universidad del Valle de Guatemala

from collections import Counter
from problema1 import wordToBits
from problema3 import *

bits = '0 1'

def ocurrency():
	mssg = wordToBits("Buenos dias Magnolia")
	count = countGram(bits, mssg)
	makeHistogram(count)

ocurrency()

