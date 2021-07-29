import matplotlib.pyplot as plt
import numpy as np

bigrams = '00 01 10 11'
trigrams = '000 001 010 011 100 101 110 111'

blist = bigrams.split(' ')
tlist = trigrams.split(' ')


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
    # Se separan los elementos
    separated = [chain[i:i+n] for i in range(0, len(chain), n)]
    for i in elements:
        counted[i] = separated.count(i)/len(chain)
        counted[i] = separated.count(i)/n
        
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

print(logicalXor("00000101", "00000011"))
# generateY(6)
# count = countGram(blist, '00000101')
# makeHistogram(count)
