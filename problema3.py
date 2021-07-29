import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from problema1 import wordToBits

bits = '0 1'
bigrams = '00 01 10 11'
trigrams = '000 001 010 011 100 101 110 111'

ulist = bits.split(' ')
blist = bigrams.split(' ')
tlist = trigrams.split(' ')

tbit = [1/2, 1/2]
tbig = [1/4 for i in range(len(blist))]
ttri = [25/200 for i in range(len(tlist))]

def logicalXor(bits1, bits2):
    res = ""

    # Se empieza por el ultimo bit
    for i in range(len(bits1)):
        # Se opera xor
        res += str(int(bits1[i]) ^ int(bits2[i]))
    return res


def countGram(elements, chain):
    counted = {}
    n = len(elements[0])
    div = len(chain)/n
    # Se separan los elementos
    separated = [chain[i:i+n] for i in range(0, len(chain), n)]
    for i in elements:
        counted[i] = separated.count(i)/div
        
    return counted


def makeHistogram(count):
    values = list(count.values())
    xtitle = list(count.keys())

    plt.bar(xtitle, values)
    plt.show()


def generateY(length):
    y = ''
    numbers = np.random.choice(2, length)
    for i in numbers:
        y += str(i)
    return y


toCount = tlist
ttemp = ttri


bword = wordToBits('ArribaLasViejasBorrachasWuu')
count = countGram(toCount, bword)
# makeHistogram(count)

# Ahora se hace normal
y = generateY(len(bword))
xored = logicalXor(bword, y)
count = countGram(toCount, xored)
# makeHistogram(count)

temp = {}
for i in range(len(toCount)):
    temp[toCount[i]] = ttemp[i]
print(temp)
makeHistogram(temp)