import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # \b specified == char are at the beginning or at the end of a word
    # re.IGNORECASE == allows for case-insensitive
    # re.findall == iterates over a string
    um_count = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_count)

if __name__ == "__main__":
    main()