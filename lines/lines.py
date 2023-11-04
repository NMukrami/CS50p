import sys

# check command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line argument")
elif  len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) == 2:
    try:
        # check sys.argv[1] end with ".py"
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                
        # count line without comment and whitespace
        count_line = 0
        for line in lines:
            if not line.isspace() and not line.lstrip().startswith("#"):
                count_line += 1
        print(count_line)

    except FileNotFoundError:
        sys.exit("File does not exist")