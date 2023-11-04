vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
text = input("Input: ")
print("Output: ", end="")

for letter in text:
    if letter in vowels:
        print("", end="")
    else:
        print(letter, end="")
print()