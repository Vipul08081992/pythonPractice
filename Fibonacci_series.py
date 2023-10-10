def findNthNumber(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        sum= findNthNumber(n-1)+findNthNumber(n-2)


    return sum

#print(findNthNumber(7))

def printtilln(n):
    a=0
    b=1
    print("Print the series:")
    print(a,b,end=" ")
    while n>2:
        sum = a+b
        a=b
        b=sum
        print(sum,end=" ")
        n=n-1

#printtilln(8)

phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}

for k,v in phone_book.items():
    print(k,":",v)


import random

print(random.randint(0,9))
print(random.__dict__)