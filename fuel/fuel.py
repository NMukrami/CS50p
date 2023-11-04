while True:
    try:
        x, y = input("Fraction: ").split("/")
        fuel = round((int(x) / int(y)) * 100)
        if fuel <= 100:
            break
    except(ValueError, ZeroDivisionError):
        continue

if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(f"{fuel}%")