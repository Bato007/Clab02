def wordToBits(word):
    cadena = ""

    for letter in word:
        wordToAscii = ord(letter)
        asciiToBinary = bin(wordToAscii)
        cadena += asciiToBinary

    return cadena

def bytesToWord(bits):
    cadena = ""
    
    for i in range(0, len(bits), 9):
        actualBits = bits[i:i+9]
        bitsToAscii = int(actualBits, 2)
        asciiToLetter = chr(bitsToAscii)
        cadena += asciiToLetter
    
    return cadena

print(wordToBits("abcdefghijklmnopqrstuvwxyz"))
print(bytesToWord("0b11000010b11000100b11000110b11001000b11001010b11001100b11001110b11010000b11010010b11010100b11010110b11011000b11011010b11011100b11011110b11100000b11100010b11100100b11100110b11101000b11101010b11101100b11101110b11110000b11110010b1111010"))
print("\n")
print(wordToBits("hola"))
print(bytesToWord("0b11010000b11011110b11011000b1100001"))
print("\n")
print(wordToBits("mequieromorir"))
print(bytesToWord("0b11011010b11001010b11100010b11101010b11010010b11001010b11100100b11011110b11011010b11011110b11100100b11010010b1110010"))