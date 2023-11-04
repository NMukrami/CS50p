import csv
import sys



def main():
    file_csv_1, file_csv_2 = command_line_argv()
    file_csv_1_in_list = csv_reader(file_csv_1)
    csv_writer(file_csv_1_in_list, file_csv_2)


# check command_line it's valid or not
def command_line_argv():
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") and len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2] #return 1.csv and 2.csv

    elif len(sys.argv) < 2 :
        sys.exit("Too few command-line argument")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


# read csv file sys.argv[1] and convert to list
def csv_reader(file_csv_1):
    try:
        file_csv_1_in_list = []
        with open(file_csv_1, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_first_name = row["name"].split(",") #split to first and last name in to one string with space beetween
                file_csv_1_in_list.append({"first_name": last_first_name[1].lstrip(), "last_name": last_first_name[0], "house": row["house"]}) #first name without whitespace
        return file_csv_1_in_list

    except FileNotFoundError:
        sys.exit(f"Could not read {file_csv_1}")


# input list and create new csv file
def csv_writer(file_csv_1_in_list, file_csv_2):
    with open(file_csv_2, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"]) #header
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in file_csv_1_in_list:
            writer.writerow({"first": row["first_name"], "last": row["last_name"], "house": row["house"]})# content of list to new csv file


if __name__ == "__main__":
    main()