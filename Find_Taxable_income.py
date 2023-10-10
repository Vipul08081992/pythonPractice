
def taxToPay(Income):
    if Income <= 10000 and Income >=0:
        return 0
    elif Income > 10000 and Income <= 20000:
        return (Income-10000)*10/100
    else:
        return 10000*10/100 + (Income-20000)*20/100


Income=float(input("Enter the taxable income in Dollor: $"))

if Income <0:
    print(("Invalid Income."))
else:
    print("Tax to pay : $",taxToPay(Income))
