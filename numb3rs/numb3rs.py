import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        numbers = ip.split(".")
        for num in numbers:
            if not int(num) in range(0,256):
                return False
        if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip): 
            return True
        else:
            return False

    except:
        return False

if __name__ == "__main__":
    main()