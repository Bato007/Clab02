# Lab 02 Criptografía
# Universidad del Valle de Guatemala

import matplotlib.pyplot as plt
from collections import Counter

tryByte = '0010010100111010111'

def ocurrency(text):
	c = Counter(text)
	return c

print(ocurrency(tryByte))