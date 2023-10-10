numbers = [4,2,7,1,8,3,6]

n= int(input("Enter the Number to find :"))
f=0
for i in range(len(numbers)):
    if numbers[i] == n:
        f = 1
        print(f''' The number is present at the location {i}.''')
        break

if f ==0:
       print("Number not present in List.")

