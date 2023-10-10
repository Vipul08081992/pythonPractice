def till_zero(n):
    if n == 0:
        return

    print(n)
    n -= 1
    till_zero(n)


def factorial(n):
    if n == 0 or n== 1:
        f=1
    else:
          f =n * factorial(n-1)
          
    return f



n = int(input("Enter the number:"))
print(factorial(n))
till_zero(n)
