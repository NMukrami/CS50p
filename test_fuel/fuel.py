def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            fuel = (int(x) / int(y)) * 100
            if fuel <= 100:
                return fuel
            else:
                pass
        except(ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if round(percentage) <= 1:
        return "E"
    elif 99 <= round(percentage) <= 100:
        return "F"
    else:
       return f"{round(percentage)}%"


if __name__ == "__main__":
    main()