
import collections as c 

l = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'a']

# to get the number of occurences of each element in a list
counter = c.Counter(l)
print(counter)# {'a': 4, 'b': 3, 'c': 2}

# to get the most common element 
print(counter.most_common(1))# the most common 1
# parameter is the number of most common elements to be returned
# return list of tuples

# to get the most common word of a string 
s = open('regex_sum_1452487.txt').read()
import re 
# convert string to list of words
words = re.findall('[a-z]+', s)
counter = c.Counter(words)
print(counter.most_common(1)[0][0])

# chain map is used to combine multiple dictionaries
# to get the value of a key from multiple dictionaries

d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

chain = c.ChainMap(d1, d2, d3)
print(chain['a'])# 1
# if key is not present in any of the dictionaries, it will return None
# if key is present in multiple dictionaries, it will return the value of the first dictionary


# namedtuple is used to create a tuple with named fields

Student = c.namedtuple('Student', 'name, age, rollno')
# form a class with named attributes

s1 = Student('John', 20, 1)# as objedt of a calss Student
print(s1.name)# John
print(s1.age)# 20
print(s1.rollno)# 1

# cnvert a list to an object of a class
l1 = ['motasem',22,1]
s2 = Student._make(l1)
print(s2.name)# motasem

# convert the object to a dictionary
d1 = s1._asdict()
print(d1)# {'name': 'motasem', 'age': 22, 'rollno': 1}