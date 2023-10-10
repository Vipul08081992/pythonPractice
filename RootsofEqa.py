print("Ax^2 +Bx +C")
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))

if a != 0:
	d = b**2 - 4*a*c
	if d > 0:
		root1= (b - (d**0.5)) /(2*a)
		root2= (b + (d**0.5)) /(2*a)
		print(f"Roots of the equation are Real: {root1} & {root2}")
	elif d == 0:
		root1 = (b - (d ** 0.5)) / (2 * a)
		print(f"Roots of the equation are equal : {root1}")
	elif d <0:
		rp = -b/(2*a)
		ip = (((-1)*d)**0.5)/(2*a)
		print(f"Roots of the equation are Not-Real : {rp} + {ip}i & {rp} - {ip}i")

else:
	print("Not a quadratic equation.")




