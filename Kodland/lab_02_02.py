print("Numbers < 10 (while):")
i = 0
while (i<10):
    print(i, end=" ")
    i += 1
print("\n")

print("Numbers < 10 (for):")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")

sum = 0
for i in range(0,100):
    if i > 10:
        print("\nWe reached the end, final sum: ", sum)
        break
    sum += i

i = 0
while i<=15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")

print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")

print("\n\n")


for j in range (500):
    if j < 300:
        if j%7 == 0:
            if j%14 == 0:
                pass
            else:
                print(j)
    else:
        break
else:
    print("All numbers were printed!")

while i < 500:
    if i < 300:
        if i%7 == 0:
            if i%14 == 0:
                pass 
            else:
                print(i)
        i += 1
    else:
        break
else:
    print("All numbers were printed!")

print("\n")

'''lst = []
for l in range(4):
    lst.append(['O'] * 4)
    lst.pop(l)
    lst.insert(l, l+1)
    lst.append(["O"] * 4)
for row in lst:
    print(' '.join(row))
'''
