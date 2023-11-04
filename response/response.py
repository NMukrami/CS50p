from validator_collection import validators, checkers, errors


def main():
    user_email = input("What's your email address? ")
    print(email_validation(user_email))

def email_validation(user):
    # checkers == check email is valid or not
    if checkers.is_email(user):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()