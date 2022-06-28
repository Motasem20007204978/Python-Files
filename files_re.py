import re
from urllib.request import urlopen

print('////////////////////////////////////////////////////////')
file = open('regex_sum_1452487.txt')
total = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    total += sum(map(int, numbers))

print(total)

#or 

data_file = urlopen('http://py4e-data.dr-chuck.net/regex_sum_1452487.txt')
data_file = data_file.read().decode()

numbers = re.findall('[0-9]+', data_file)
total += sum(map(int, numbers))

print(total)
