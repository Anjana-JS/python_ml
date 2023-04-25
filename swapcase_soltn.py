#Given a string, task is to swap cases.
#Method 1:
k = ""
t = input("Enter the string, please ")
for i in t:
    if i.islower():
        k+=i.upper()
    else:
        k+=i.lower()
print(k)

