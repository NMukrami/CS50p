import random


def main():
    level = get_level()
# get score and 10 random question
    game_score = 0
    for i in range(10):
        x, y = generate_integer(level)
        if check_the_answer(x, y):
            game_score += 1
    print(f"Score: {game_score}")


# check the answer, if wrong get 3 attempt to answer
def check_the_answer(x, y):
    attempt_to_answer = 0
    while attempt_to_answer < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (int(x) + int(y)):
                return True
            else:
                attempt_to_answer += 1
                print("EEE")
        except:
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


# check the level from user in range number 1 to 3
def get_level():
    while True:
        lvl = input("Level: ")
        try:
            if 1 <= int(lvl) <= 3:
                return int(lvl)
            else:
                pass
        except:
            pass


# generate number(x, y) based on level from user
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 90)
        y = random.randint(10, 90)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return int(x), int(y)


if __name__ == "__main__":
    main()