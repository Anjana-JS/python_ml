dict = {}
for i in range(int(input("Enter the limit : "))):
    item, space, price = input("Enter the item and corresponding price with space in between").rpartition(' ')
    dict[item] = dict.get(item,0) + int(price)

for item, price in dict.items():
    print(item,price)




