from tabulate import tabulate
import csv
import sys


def main():
    file_name = command_line_argv()
    csv_reader(file_name)

# check command_line it's valid or not
def command_line_argv():
    if  len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line argument")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        return sys.argv[1]

# read csv file and convert to list, after that to table(tabulate)
def csv_reader(file_name):
    try:
        menu = []
        with open(file_name, "r") as file:
            file_csv = csv.reader(file)
            for row in file_csv:
                menu.append(row)
        print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()