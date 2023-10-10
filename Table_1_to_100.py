def Table(num):
    print(num, end=" ")
    for i in range(1,11):
        print(num*i,end=" ")

for i in range(1,11):
    Table(i)
    print("\n")
