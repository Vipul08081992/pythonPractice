def checkArmstrong(num):
    flag=False
    p= countDigit(num)
    if num == sumpowerDigits(num,p):
        flag =True
    return flag

def listofArmstrong(l,h):
    arm = []
    for num in range(l, h):
        if checkArmstrong(num):
            arm.append(num)
    return arm
def largestArmstronginrange(arm):

    largest=arm[0]
    for i in range(1,len(arm)):
        if arm[i] > largest:
            largest=arm[i]
    return largest





def smallestArmstronginrange(arm):
    smallest = arm[0]

    for i in range(1, len(arm)):
        if arm[i] < smallest:
            smallest = arm[i]

    return smallest
def countDigit(num):
    count=0
    while num >0:
        count +=1
        num //=10
    return count

def sumpowerDigits(num,p):
    sum=0
    while num>0:
        sum += (num%10)**p
        num //=10


    return sum


print(''' Choose:
            A - Check a number is armstrong or not.
            B - Largest in the range.
            C - Smallest in range.
            D - List of armstrong in range.
            ''')
Cho= input('Enter the choice: ')
if Cho.upper() == 'A':
    if checkArmstrong(int(input("Enter the number:"))):
         print("Is a Armstrong Number.")
    else:
        print("Is not a Armstrong Number.")

elif Cho.upper() == 'B':
    l =int(input("Enter the lower limit :"))
    h = int(input("Enter the upper limit :"))
    arm= listofArmstrong(l,h)
    print(f"Largest Armstrong number in range {l} to {h} :",largestArmstronginrange(arm))
elif Cho.upper() == 'C':
    l =int(input("Enter the lower limit :"))
    h = int(input("Enter the upper limit :"))
    arm= listofArmstrong(l,h)
    print(f"Smallest Armstrong number in range {l} to {h} :",smallestArmstronginrange(arm))
elif Cho.upper() == 'D':
    l =int(input("Enter the lower limit :"))
    h = int(input("Enter the upper limit :"))
    print(f"List of armstrong number in range {l} to {h}: ",listofArmstrong(l,h))
else:
    print("Invalid choice.")