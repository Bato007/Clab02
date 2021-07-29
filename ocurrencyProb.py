# Lab 02 Criptografía
# Universidad del Valle de Guatemala

from collections import Counter
from problema1 import wordToBits
from problema3 import makeHistogram

bits = '0 1'

def countGram(elements, chain):
    counted = {}
    n = len(elements[0])
    # Se separan los elementos
    separated = [chain[i:i+n] for i in range(0, len(chain), n)]
    for i in elements:
        counted[i] = separated.count(i)/len(chain)
        
    return counted



def ocurrency():
	mssg = wordToBits("ArribaLasViejasBorrachas")
	count = countGram(bits, mssg)
	makeHistogram(count)

ocurrency()

