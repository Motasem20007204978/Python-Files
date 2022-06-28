
def splitNum(num:int, dividor:int)->list:
    
    string = str(num).zfill(dividor*2)
    returned = list(string[i:i+dividor] for i in range(0, dividor*2, dividor))
    return returned

#multiple tow huge numbers algorithm
def Karatsuba(n1:int, n2:int)->int:

    if n1 in range(10) and n2 in range(10):
        return n1 * n2    

    dividor = (max(len(str(n1)), len(str(n2))) + 1)//2

    a,b = splitNum(n1, dividor)
    a = int(a); b = int(b)
    c,d = splitNum(n2, dividor)
    c = int(c); d = int(d)

    A = Karatsuba(a,c)
    B = Karatsuba(b,d)
    C = Karatsuba(a+b, c+d)
    C_sub_A_B = C - (A + B)
    z = 10**dividor

    result = A*z**2 + B + C_sub_A_B*z
    return result

#opposite decimal digit to binary digit
def DecNumberOppositeToBi(bi:str)->list:
    Bits = [128,64,32,16,8,4,2,1]
    SplittedBits = Bits[-len(bi):]
    return list(SplittedBits[i] for i in range(len(bi)) if int(bi[i]))
    
#exponent tow huge number algorithm
def exp_by_squaring(x, n):
    if n == 1: 
        return x
    elif not n%2: 
        return exp_by_squaring(Karatsuba(x,x),  n // 2)
    else: 
        y = exp_by_squaring(Karatsuba(x,x), n // 2)
        return Karatsuba(x,y)
        


print(55**59)
print(exp_by_squaring(55,59))
