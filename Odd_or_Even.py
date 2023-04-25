#First problem

n = int(input("Enter a number"))
if n%2==0:
    print("Your number is even,bud!")
else:
    print("Your number is odd,bud!")

#Second problem:- If n is odd,print "Weird". If n is even and in the inclusive range of 2 to 5, print "Not Weird".
#If n is even and in the inclusive range of 6 to 20,print "Weird". If n is even greater than 20, print "Not Weird".

n = int(input("enter your number"))
if n%2!=0:
    print("Weird")
elif n%2==0:
    if n in range (2,6):
        print("Not Weird")
    if n in range (6,21):
        print("Weird")
    if n>20:
        print("Not Weird")
