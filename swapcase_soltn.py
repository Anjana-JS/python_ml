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

#Method 2: Let's create a function,dear one :)

def swapi(k):
    k = ""
    for i in text:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    print(k)
text = input("My text to swap the cases is: ")
swapi(text)

