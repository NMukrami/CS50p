import random

while True:
    try:
        level = int(input("Level: "))
        answer = random.randint(1, level)
        # check level number if positive or negative
        if level > 0 :
            #  check guess if it's int or str
            guess = int(input("Guess: "))
            # check guess number if positive or negative
            if guess > 0:
                if guess > answer:
                    print("Too large!")
                elif guess < answer:
                    print("Too small!")
                elif guess == answer:
                    print("Just right!")
                    break
            else:
                pass
        else :
            pass
    except:
        print()
        pass