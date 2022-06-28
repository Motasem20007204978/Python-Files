
string = "5462"
print(string.isnumeric())#True

string = "moTasEm anwar"
print(string.rstrip())#remove white space

print(string.swapcase())#swap character by character

print(string.title())
#convert the first character to upper and all remaining characters lower in each word
print(string.zfill(10))
#fill the string with zeros untill the length become as parameter
print(string.split())#split the string to list, each word in an index
print(" ".join(string.split()))#join is opposite of split

print(f"{5.636:9.2f}")

def F2C(T:int)->float:
    return (T-32)*5/9

for T in range(0,100,10):
    print(f"{T} F | {F2C(T):<8.2f}C")

#to change in the string
print(string.replace("o", "l"))

def odd(n):
    return n%3
print(odd(5))

print(5000%60)
prefix = "Ana"
string = string.__add__("mo")
print(string)
print(string.removeprefix("mo"))
#if there is more than one string as mo, it removes only first

LOT = enumerate(string)#[(0,"m"), (1,"o"), (2,"t")....] list of tuples 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for i,e in enumerate(filenames):
    if e.endswith(".hpp"):        
        filenames[i] = e.rstrip("hpp")+"h"
print(filenames)

def pig_latin(text:str)->str:
    lis = text.split()
    for i,e in enumerate(lis):
        lis[i] = e[1:] + e[0] + "ay"

    return " ".join(lis)

print(pig_latin("hello how are you"))

print('motasem'.__contains__('m'))
        