word = input("camalCase: ")
print("snake_case: ", end="")
for letter in word:
    if letter.isupper():
        print(f"_{letter.lower()}", end="")
    else:
        print(letter, end="")
print()