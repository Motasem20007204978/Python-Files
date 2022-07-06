
from sympy import factorint

def has_Kprimes_nums( min_num, max_num, k):
    nums = []
    for num in range(min_num, max_num + 1):        
        if sum(factorint(num).values()) == k:
            nums.append(num)
    return nums


# Numbers that are divisible by exactly k primes
# https://en.wikipedia.org/wiki/K-primes
# https://oeis.org/A001328
# https://oeis.org/A001328/a001328.txt
# https://oeis.org/A001328/a001328_1.txt

if __name__ == '__main__':
    print(has_Kprimes_nums(1, 100, 2))
    print(has_Kprimes_nums(1, 100, 5))
    print(has_Kprimes_nums(1, 100, 6))