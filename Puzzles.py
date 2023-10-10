'''
def findin(i):
    count19=0
    count5=0
    for a in i:

        if a==19:
            count19 +=1
        elif a==5:
            count5 +=1


    if count19 == 2 and count5 >=3:
        return True
    else:
        return False

def num195(num):
    if num.count(5) >=3 & num.count(19) == 2:
        return True
    else:
        return False


print(findin([19, 19, 15, 5, 3, 5, 5, 2]))
print(findin([19,15,15,5,3,3,5,2]))
print(findin([19,19,5,5,5,5,5]))

print(num195([19, 19, 15, 5, 3, 5, 5, 2]))
print(num195([19,15,15,5,3,3,5,2]))
print(num195([19,19,5,5,5,5,5]))


def test3(num):

    if len(num) ==8 and num.count(num[4]) == 3:
        return True
    else:
        return False

print(test3([19, 19, 15, 5, 5, 5, 1, 2]))
print(test3([[19, 15, 5, 7, 5, 5, 2]]))
print(test3([11, 12, 14, 13, 14, 13, 15, 14]))
print(test3([19, 15, 11, 7, 5, 6, 2]))
'''
'''
def test4(num):
    if num > 4**4 and num % 34 == 4:
        return True
    else:
        return False

print(test4(int(input("Enter the number: "))))

'''

