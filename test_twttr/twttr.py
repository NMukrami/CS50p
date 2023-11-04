def main():
    text = input("Input: ")
    print("Output: ", end="")
    final_word = shorten(text)
    print(final_word)

def shorten(word):
    no_vowel = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter.lower() in vowels:
            no_vowel += ""
        else:
            no_vowel += letter
    return no_vowel

if __name__ == "__main__":
    main()