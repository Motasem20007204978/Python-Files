# Python3 code to implement Hill Cipher
import numpy as np

#keyMatrix = [[0] * 3 for i in range(3)]
keyMatrix = np.array([[1,2,12],[8,5,6],[9,3,5]])#fill it if key was matrix immediately

# Generate vector for the message
messageVector = [[0] for i in range(len(keyMatrix))]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(len(keyMatrix))]

# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(len(keyMatrix)):
		for j in range(len(keyMatrix)):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message
def encrypt(messageVector):
	for i in range(len(keyMatrix)):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(len(keyMatrix)):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

from string import ascii_uppercase

def HillCipher(message:str, key):

	# Get key matrix if key was string
	#getKeyMatrix(key)

	# Generate vector for the message
	for i in range(len(keyMatrix)):
		messageVector[i][0] = ascii_uppercase.index(message[i].upper())

	# Following function generates
	# the encrypted vector
	encrypt(messageVector)

	# Generate the encrypted text
	# from the encrypted vector
	CipherText = []
	for i in range(len(keyMatrix)):
		CipherText.append(ascii_uppercase[cipherMatrix[i][0]])

	# Finally print the ciphertext
	print("Ciphertext: ", "".join(CipherText))

# Driver Code
def main():

	# Get the key
	key = "GYBNQKURP"
	#remove the comment from HillCipher method above for getKeyMatrix called method if key was string

	message = "Eng"
	HillCipher(message, key)
	message = "ine"
	HillCipher(message, key)
	message = "Ers"
	HillCipher(message, key)

if __name__ == "__main__":
	main()
