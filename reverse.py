# Simple reverse Cipher

message = input('Enter a message: ')

def reverseCipher(message):
	translated = ''
	i=len(message)-1
	while i>=0:
		translated+=message[i]
		i-=1
	print(translated)


reverseCipher(message)
