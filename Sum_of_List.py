def sum_list(n):
    number=[]

    for i in range(n):

        x= int(input("Enter the Number: "))
        number.append(x)

    print("Sum of Number:",sum(number))


sum_list(int(input("Enter the Size of list:")))
