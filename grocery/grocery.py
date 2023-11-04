grocery_list = {}

while True:
    try:
        item = input().upper()

        #if item already in dict add 1 to value
        if item in grocery_list:
            grocery_list[item] += 1

        #if item not in dict add key(item) & value(1)
        else:
            grocery_list[item] = 1
    except EOFError:
        break

#sort dict & print item(value), key(item)
for item in sorted(grocery_list):
    print(grocery_list[item], item)