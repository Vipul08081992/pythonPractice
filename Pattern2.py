def pattern2():
    for i in range(5,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")

#pattern2()

def exponent(base, exp):
    print(f'''
    base = {base}
exponent = {exp}

{base} raises to the power of {exp}: {base**exp} i.e. ( {f"{base} *"*(exp-1)}{base} = {base**exp})''')

exponent(5, 4)