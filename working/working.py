import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    times = re.search(r"^([0-9]{1,2}):?([0-9]{0,2}) (AM|PM) to ([0-9]{1,2}):?([0-9]{0,2}) (AM|PM)$", s)
    if times:
        var = times.groups()

# if min is None assign it to int 0
        min_1 = var[1]
        if min_1 == "":
            min_1 = int(0)
        min_2 = var[4]
        if min_2 == "":
            min_2 = int(0)

# if min more than 60, raise
        if int(min_1) >= 60 or int(min_2) >= 60:
            raise ValueError

# if PM convert to 24 hours system
        hours_1 = int(var[0])
        if var[2] == "PM":
            hours_1 += 12

# if 12 AM convert to 24 hours system
        if var[2] == "AM" and hours_1 == 12:
            hours_1 = 0

# if PM convert to 24 hours system
        hours_2 = int(var[3])
        if var[5] == "PM" and hours_2 == 12:
            hours_2 = 12

# if 12 PM convert to 24 hours system
        if var[5] == "PM" and not hours_2 == 12:
            hours_2 += 12

        return  f"{hours_1:02}:{min_1:02} to {hours_2:02}:{min_2:02}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()