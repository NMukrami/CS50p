import inflect

p = inflect.engine()

my_list = []
while True:
    try:
        name = input("Name: ")
        my_list.append(name)
        list_name = p.join(my_list)
    except:
        print()
        print(f"Adieu, adieu, to {list_name}.")
        break