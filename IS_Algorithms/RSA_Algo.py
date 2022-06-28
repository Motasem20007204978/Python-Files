from string import ascii_lowercase

def modInverse(e, n):     
    for x in range(1, n):
        if e * x % n == 1:
            return x
    return -1

def encrypt(me,e,n):
    c = me**e%n
    print(c, end=" ")
    return int(c)

#variables to be changed 
p,q = 11,17
rpubkey = 13#reciever public key
spubkey = 43#sender public key

#variables calculated with some operation
n = p*q
fi_n = (p-1)*(q-1)
sprikey = modInverse(spubkey,fi_n)#sender private key
rprikey = modInverse(rpubkey,fi_n)#reciever private key

print(f"Multiplicative Inverse or decryption (private) key for sender {spubkey} is {sprikey}")
print(f"Multiplicative Inverse or decryption (private) key for reciever {rpubkey} is {rprikey}")

message = input("Enter the message to be encrypted: ")

indecies = list(ascii_lowercase.index(ch.casefold()) for ch in message)

#/////////////////////////////////////////////////////

cipher = []
print('Encryption using confidentiality:', end=" ")
for index in indecies:
    cipher.append(encrypt(index,rpubkey,n))

print("\nafter decryption: ", end="")
for c in cipher:
    print(ascii_lowercase[c**rprikey%n], end="")

#///////////////////////////////////////////////////////

cipher = []
print('\nEncryption using authenticaion:', end=" ")
for index in indecies:
    cipher.append(encrypt(index,sprikey,n))

print("\nafter decryption: ", end="")
for c in cipher:
    print(ascii_lowercase[c**spubkey%n], end="")

#//////////////////////////////////////////////////////////

cipher = []
print("\nuse both authenticaton and confidentiality to encrypt :")
for ind in indecies:
    c = (ind**sprikey%n)**rpubkey%n
    cipher.append(c)
    print(c, end=" ")

print("\nuse both authenticaton and confidentiality to decrypt :")
for i in cipher:
    p = ascii_lowercase[(i**rprikey%n)**spubkey%n]
    print(p, end="")

