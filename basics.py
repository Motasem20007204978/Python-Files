import sys 

sys.stdout.write("Hello World!\n")
sys.stdout.flush()
#as
print('Hello World!', flush=True)# end = '\n'

import time

# we can use it to check the time spent on executing the function
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return wrapper


# print list of numbers with separator between each number
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*l, sep='>>')
# as above but with end='\n'
s = '>>'.join(str(i) for i in l)
print(s)

# any function can be decorated with timer function
@timer
def counter():
    for i in reversed(range(1, 11)):
        print(i, sep='>>')
        time.sleep(.1)

counter()

def check_time_spent(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
    return wrapper

@check_time_spent
def check_duplicates(List:list):
    for i in List:
        if List.count(i) > 1:
            return True
    return False

@check_time_spent
def check_duplicates_set(List:list):
    return len(set(List)) != len(List)

@check_time_spent
def check_duplicates2(List:list):
    return any(lambda x: x.count(x) > 1 for x in List)


check_duplicates(range(500000))
check_duplicates_set(range(500000))
check_duplicates2(range(500000))

# to check the highest number occuring in the list
@check_time_spent
def mode(List:list):
    numbers = set(List)
    mode = max(numbers, key=List.count)
    return mode 

print(mode(range(500000)))

'''
hello my friends 
my name is motasem 
i am a student
my age is 22
my decipline is softare engineering
my hobbies are playing games and reading books
my favorite food is pizza
my favorite color is black
my favorite movie is the matrix
my favorite song is the one that i like the most

i am learning python for web development
i will leatn django framework
i will use artifical intelligence libraries
maciane learning is very important.

'''
