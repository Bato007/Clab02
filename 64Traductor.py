# Lab 02 Criptografía
# Universidad del Valle de Guatemala

import base64


def encode64(text):
	mssgBytes = text.encode('ascii')
	b64_bytes = base64.b64encode(mssgBytes)
	b64_str = b64_bytes.decode('ascii')

	return b64_str

def decode64(b64_str):
	b64_bytes = b64_str.encode('ascii')
	mssgBytes = base64.b64decode(b64_bytes)
	mssg = mssgBytes.decode('ascii')
	
	return mssg

# Examples
# "apples"
print('\nEXAMPLES')
print('---------------------------------')
aux = encode64('apples') # Encoding
print(aux)
print(decode64(aux)) # Decoding
print('---------------------------------')
aux = encode64('pencil') # Encoding
print(aux)
print(decode64(aux)) # Decoding
print('---------------------------------')
aux = encode64('cryptography') # Encoding
print(aux)
print(decode64(aux)) # Decoding
