user_fruit = input("Item: ").lower()

list_of_fruits = {
    "apple": "130",
    "avocado": "50",
    "kiwifruit": "90",
    "pear": "100",
    "sweet cherries": "100",
    }

for item_calories in list_of_fruits:
    if item_calories in user_fruit:
        print("Calories: " + list_of_fruits[item_calories])