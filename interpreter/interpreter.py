x, y, z = input("Expression: ").split(" ")

if "+" in y:
    print(float(x) + float(z))
elif "-" in y:
    print(float(x) - float(z))
elif "*" in y:
    print(float(x) * float(z))
elif "/" in y:
    print(float(x) / float(z))