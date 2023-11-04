from seasons import min_since_born, num_to_words
import pytest


def main():
    test_min_since_born()
    test_num_to_words()

def test_min_since_born():
    assert min_since_born("2000-04-30") == 12320640

def test_num_to_words():
    assert num_to_words(12320640) == "Twelve million, three hundred twenty thousand, six hundred forty minutes"


if __name__ == "__main__":
    main()