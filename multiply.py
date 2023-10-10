
def mulAdd(x,y):
    if (x*y) < 1000:
        print("The result is ",x*y)
    else:
        print("The result is ", x + y)

#mulAdd(20,30)
#mulAdd(40,30)

def iteration():
    print('''Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0''')
    sum=1
    for i in range(1,10):
        sum = (i-1) +i
        print(f"Current Number {i} Previous Number  {i-1}  Sum:  {sum}")


#iteration()

def stringEvenIndex(text):
    for i in range(0,len(text),2):
        print(text[i])

#stringEvenIndex(input("Input String: \n"))

def stringRemoveFirst(text,x):
     print(text[x:])

#stringRemoveFirst(input("Input String: \n"),int(input("Input Number of character to remove: \n")))

def checkFirstLast(x):
    if x[0] == x[-1]:
        return True
    else:
        return False

'''
numbers_x = [10, 20, 30, 40, 10]
print(numbers_x)
print("result is",checkFirstLast(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print(numbers_y)
print("result is",checkFirstLast(numbers_y))
'''
def divisibleBy5():
    num_list = [10, 20, 33, 46, 55]
    print("Given list:", num_list)
    print('Divisible by 5:')
    for i in num_list:

        if int(i) % 5 == 0:
            print(i)


#divisibleBy5()

def stringCount():
    str_x = "Emma is good developer. Emma is a writer"
    List= str_x.split(" ")
    count=0
    for i in List:
        if  i == "Emma" :
            count += 1
    print( f"Emma appeared {count} times")

#stringCount()

def pattern1():
    for i in range(1,6):
        for j in range(i):
            print(i,end=" ")
        print("\n")

#pattern1()

def palindrome(number):
    print("original number", number)
    original_num = number
    reverse_num=0
    while original_num > 0:
        reverse_num =(reverse_num*10) + (original_num % 10)
        original_num //= 10
    print("Reversed number", reverse_num)

#palindrome(121)
#palindrome(125)

def mergeList(List1,List2):
    List3=[]
    for i in List1:
        if i % 2 != 0:
            List3.append(i)
    for i in List2:
        if i % 2 == 0:
            List3.append(i)

    return List3

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("result list:",mergeList(list1,list2))

def ReverseOrder(number):
    print("original number", number)
    original_num = number

    while original_num > 0:
        reverse_num = original_num % 10
        print(reverse_num,end=" ")
        original_num //= 10


ReverseOrder(int(input("Enter the Number : \n")))