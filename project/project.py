import requests
import random
import html
from art import *
import cowsay


def main():
    Art=text2art("Welcome",font='block',chr_ignore=True)
    print(Art)
    score, question_amount = play_game()
    scores = final_score(score, question_amount)
    cowsay.cow(f"{scores}")
    print()

# start the game
def play_game():
    score = 0
    question_number = 1
    question_amount = amount_question()
    print()
    questions = get_question(question_amount)
    for question in questions:
        question_ask = html.unescape(question["question"])

        print(f"{question_number}) {question_ask} ")
        question_number += 1

        choices = question["incorrect_answers"]
        choices.extend([question["correct_answer"]])

        shuffle_option = randomize_options(choices)
        display_choices(shuffle_option)

        user_choice =  get_user_input()
        user_answer = shuffle_option[user_choice]
        correct_answer = html.unescape(question["correct_answer"])

        if answer_checker(user_answer, correct_answer) == True:
            print(f"You got it right!\n")
            score += 1
        else:
            print(f"That's wrong!\nCorrect answer is: {correct_answer}\n")

    return score, question_amount

# Get the user score by answering the correct answer
def final_score(score, question_amount):
    scores = f"Your Score is: {score}/{question_amount}"
    return scores

# Get the amount of question 1-50 and check if it is an integer or not
def amount_question():
    while True:
        try:
            get_amount = input("How many question do you want (1-50): ")
            if 1 <= int(get_amount) <= 50:
                return get_amount
            else:
                print("Number between 1 and 50")
        except ValueError:
            print(f"Not a number: {get_amount}")

# Get an answer from the user between 1 and 4
def get_user_input():
    while True:
        try:
            user_input = input("Please enter your answer (1-4): ")
            if 1 <= int(user_input) <= 4:
                return int(user_input) - 1
            else:
                print("Please enter a number between 1 and 4")
        except ValueError:
            print(f"Not a number: {user_input}")

# print the questions
def display_choices(options):
    for number_choice, choice in enumerate(options, start=1):
        print(f"{number_choice}. {html.unescape(choice)}")

# Check if the user's answer is correct or incorrect
def answer_checker(user_answer,correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False
# randomly generate the choices of answer
def randomize_options(choices):
    random.shuffle(choices)
    return choices

# ask users how many questions they want
def get_question(amount):
    api_url = requests.get(f"https://opentdb.com/api.php?amount={amount}&category=18&type=multiple")
    response = api_url.json()
    return response["results"]


if __name__ == "__main__":
    main()
