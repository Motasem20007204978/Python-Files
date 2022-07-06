import random


import time 

# check time complexity of each algorithm with wrapper to find the best 
def check_time_spent(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(func.__name__, (end - start).real)
    return wrapper

'''
find the maximum product of two distinct numbers in an array of integers
'''
@check_time_spent
def max_pairwise_product(numbers:list) -> int:
    numbers.sort()
    return numbers[-1] * numbers[-2]

@check_time_spent
def max_pairwise_product_2(numbers:list) -> int:
    max_product = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product
    

# stress test
# compare more than one algorithm to find the best one for the given input
def stress_test(n:int) -> None:
    while True:
        numbers = [random.randint(0,100) for _ in range(n)]
        print(numbers)
        result1 = max_pairwise_product(numbers)
        result2 = max_pairwise_product_2(numbers)
        if result1 != result2:
            print("error")
            print(result1, result2)
            break

        print("\n")


n = random.randint(2,10)
# stress test
# stress_test(n)
numbers = [random.randint(0,100) for _ in range(n*1000)]

max_pairwise_product(numbers)
max_pairwise_product_2(numbers)