def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # minimum of 2 char
    if len(s) < 2:
        return False

    # maximum of 6 char
    if len(s) > 6:
        return False

    # check for symbol(spaces and punctuation)
    for symbol in s:
        if symbol == ".":
            return False

    # Numbers cannot be used in the middle of a plate; they must come at the end
    for num in s:
        if not num.isalpha():
            if num == "0":
                return False
            if s[-1] == "2":
                return False
            else:
                break

    #check for index 0 in string
    if s[0].isalpha():
        return True

    #check for index 1 in string
    if s[1].isalpha():
        return True

    return True

main()