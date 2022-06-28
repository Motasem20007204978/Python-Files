#A python program to illustrate Caesar Cipher Technique
def encrypt(text,key):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + key-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + key - 97) % 26 + 97)

	return result

#check the above function
text = "ENGINEER"
key = 13
print("Text : " + text)
print("Shift : " + str(key))
print("Cipher: " + encrypt(text,key))
