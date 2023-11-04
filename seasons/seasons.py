from datetime import date
import inflect
import sys


def main():
    minutes = min_since_born(input("Date of Birth: "))
    duration = num_to_words(minutes)
    print(duration)


# check dates is valid or not, if not sys.exit, and then convert to minutes
def min_since_born(dates):
    try:
        year, month, day = dates.split("-")
        today = date.today()
        date_born = date(int(year), int(month), int(day))
        period = today - date_born
        minutes = period.total_seconds() / 60 #second to minutes
        return int(minutes)

    except ValueError:
        sys.exit("Invalid date")


# get argument and convert minutes to words in inflect
def num_to_words(num):
    p = inflect.engine()
    words = p.number_to_words(num, andword="")
    duration = words.capitalize() + " minutes"
    return duration


if __name__ == "__main__":
    main()