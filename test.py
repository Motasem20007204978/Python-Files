import requests
print( requests.get("http://www.google.com"))
print('motasem'.encode(encoding='utf-16'))

num = 82528
print(str(num) == str(num)[::-1])

print(chr(108),chr(105),chr(110),chr(101))
print(ord('G'))

def ID(id):
	id = 5
	return id

print(ID(9))


import operator

l1 = [5,8,1,3]
l2 = [9,12,4,31]

l3 = list(map(operator.add, l1, l2))#adding elements in parallel
l3 = list(map(operator.truediv, l1, l2))#division of elements in parallel
l3 = list(map(operator.sub, l1, l2))#subtracting elements in parallel
l3 = list(map(operator.mul, l1, l2))#multiplying elements in parallel
#l3 as same length as smaller list

for i in range(1000):
	if False:
		break
else:
	print('loop reaches to end because break statement not be executed')

import subprocess
print(subprocess.run(['host', '8.8.8.8'], capture_output=True))