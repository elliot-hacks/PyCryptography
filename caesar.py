import pyperclip
message=input("Enter a message: ")
key=int(input("Enter a key: "))
mode=input("Enter a mode\n(a) encrypt\n(b) decrypt\n\t ")


def caesarCipher(message, key, mode):
	LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated=''
	message=message.upper()
	
	for letter in message:
		if letter in LETTERS:
			num=LETTERS.find(letter)
			if mode=='encrypt' or mode=='a' or mode=='(a)':
				num+=key
			elif mode=='decrypt' or mode=='b' or mode=='(b)':
				num-=key
			if num>=len(LETTERS):
				num-=len(LETTERS)
			elif num<0:
				num+=len(LETTERS)
			translated+=LETTERS[num]
		else:
			translated+=letter
	print(translated)
	pyperclip.copy(translated)


caesarCipher(message, key,  mode)
