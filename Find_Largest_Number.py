
def largestInList(numbers):
    largest=numbers[0]
    index =0
    for i in range(1,len(numbers)):
        if numbers[i] > largest :
            largest = numbers[i]
            index =i


    return largest , index

numbers = [3,8,1,7,2,9,5,4]
largest,index= largestInList(numbers)
print(f"Largest number in list is {largest} with index as {index}")