for i in range(1,5):
    for j in range(i):
        print(i, end =" ")
    print()

for i in range(1,5):
    for j in range(i):
        print(j+1,end = " ")
    print()

for i in range(1,5):
    for j in range(5-i):
        print(i, end=" ")
    print()

for i in range(1,5):
    for j in range(i,5):
        print(i, end = " ")
    print()

for i in range(1,7):
    for j in range(i):
        print("*", end = " ")
    print()

for i in range(1,8):
    for j in range(1,8):
        if i == 7 or j == 1 or i==j:
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print()

