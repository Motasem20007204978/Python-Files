q=29;a=11
li = []
X_A = 3; X_B = 2

def generate():
    for c,x in enumerate(range(1,q)):
        Y = a**x%q
        print(f"{c+1}: {Y}")
        li.append(Y)

generate()

Y_A = li[X_A-1];print(f"Y_A = {Y_A}")
Y_B = li[X_B-1];print(f"Y_B = {Y_B}")

print(f"K_A_B = Y_A**X_B = {Y_A**X_B%q} = Y_B**X_A = {Y_B**X_A%q}")
