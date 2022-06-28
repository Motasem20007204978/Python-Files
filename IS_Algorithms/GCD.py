
c = 0
def GCD(A:int, B:int)->int:

    global c; c += 1
    print(f"Step {c} --> A = {A}, B = {B}")

    if B == 0:        
        return A
    
    print("A = B, B = A%B")
    return GCD(B, A%B)


print(f"GCD is {GCD(65,816)}")
