def wordToBits(word):
    cadena = ""
    listOfBits = [bin(ord(x))[2:].zfill(8) for x in word]

    for bit in listOfBits:
        cadena += bit
    
    return cadena

def bytesToWord(bits):
    cadena = ""
    
    for i in range(0, len(bits), 8):
        actualBits = bits[i:i+8]
        bitsToAscii = int(actualBits, 2)
        asciiToLetter = chr(bitsToAscii)
        cadena += asciiToLetter
    
    return cadena

print(wordToBits('Hola mundo'))
print(bytesToWord('01001000011011110110110001100001001000000110110101110101011011100110010001101111'))
