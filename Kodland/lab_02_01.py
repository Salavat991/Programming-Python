num = int(input("How many times have you been to Hermitage?"))

if num > 0:
	print("Wonderful!")
	print("I hope you liked this museum!")
else:
	print("You should definitely visit Hermitage!")

course = int(input("What is your course number?"))

if course == 1:
	print("You are just at the beginning!")
elif course == 2:
	print("You learned many things, but not all of them!")
elif course == 3:
	print("The basic course is over, it's time for professional disciplines!")
else:
	print("Oh! You need to hurry! June is the month of thesis defence")

x = 5
y = 12
if y % x > 0 : print("%d cannot be evenly divided by %d" % (y, x))

z = 3
x = "{} is a divider of {}".format(z, y) if y%z == 0 else "{} is not a divided of {}".format(z, y)
print(x)
print("\n\n")

p = 0
if p > 10:
	print(p)

print(p) if p>10 else False 

a = 157
b = 525
if a > b:
	print(a % b)
elif a < b:
	print(b % a)
else:
	print(a*b)