def checkLeapyear(y):
    leap =False
    if y%400 == 0:
        leap=True
    elif y%4 == 0:
        leap = True

    return leap

y=int(input("Year to check:"))
if checkLeapyear(y):
    print("It is leap year.")
else:
    print("It is not a leap year.")

