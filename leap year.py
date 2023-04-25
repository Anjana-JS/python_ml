# Problem: Identify a leap year

def ly(year):
    if year%4 != 0:
        print("Ah!Definitely not a leap year")
    elif year%4 ==0:
        if year%100 !=0 | year%400 != 0:
            print("Not a leap year")
        else:
            print("It's a leap year")
year = int(input("Enter a year, please"))
ly(year)