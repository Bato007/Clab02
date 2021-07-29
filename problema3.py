def logicalXor(bits1, bits2):
    res = ""

    # Se empieza por el ultimo bit
    for i in range(len(bits1)):
        # Se opera xor
        res += str(int(bits1[i])^int(bits2[i]))
    return res

print(logicalXor("00000101", "00000011"))