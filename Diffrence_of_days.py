from datetime import date

a= tuple(input("Enter first date in format Y,M,D").split(','))
b= tuple(input("Enter second date in format Y,M,D Bigger than first").split(','))

f=date(int(a[0]),int(a[1]),int(a[2]))
s=date(int(b[0]),int(b[1]),int(b[2]))

diff= s-f
print(diff.days)
