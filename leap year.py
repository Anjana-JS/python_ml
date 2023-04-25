# Problem: Identify a leap year

def ly(year):
    if year%4 != 0:
        print("Ah!","not a leap year")
    elif year%100 ==0:
        if year%400 == 0:
            print("It's a leap year")
        else:
            print("Not a leap year")
year = int(input("Enter a year, please"))
ly(year)


