def main():
    greet = input("Greeting: ")
    greeted = value(greet)
    print(f"${greeted}")

def value(greeting):
    if "Hello" in greeting:
        return 0
    elif ("Hey" in greeting ) or ("How" in greeting):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()