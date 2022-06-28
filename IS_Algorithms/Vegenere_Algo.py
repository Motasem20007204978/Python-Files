from string import ascii_uppercase, digits

Letters = list(ascii_uppercase)
Digits = list(digits)
Letters.extend(Digits)#at a way digits is requested
Mix = Letters# maybe only letters
base = len(Mix)#to be used in mod operation

def cipherText(plain:str, key:str):
    cipher_text = ""
    for i in range(len(plain)):
        x = (Mix.index(plain[i].upper()) +
			Mix.index(key[i].upper())) % base
        
        cipher_text += Mix[x]
        
    return cipher_text


def originalText(cipher_text:str, key:str):
	plain_text = ""
	for i in range(len(cipher_text)):
		x = (Mix.index(cipher_text[i]) -
			Mix.index(key[i].upper()) + base) % base
		plain_text += Mix[x]
		
	return plain_text
	

plain = "ics1928"
key = "Covid19"
cipher_text = cipherText(plain, key)
print("Ciphertext :", cipher_text)
print("Original/Decrypted Text :",
    originalText(cipher_text, key))
