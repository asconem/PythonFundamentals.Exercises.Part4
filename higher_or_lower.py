def get_user_guess():
    user_guess = int(input("Enter a number between 0 an 10: "))
    while user_guess < 0 or user_guess > 10:
        user_guess = int(input("Invalid number. Enter a number between 0 an 10: "))
    return user_guess


def get_random_number():
    from random import randrange
    return randrange(1, 11)


def evaluate_result():
    user = get_user_guess()
    computer = get_random_number()
    while user != computer:
        if user > computer:
            user = int(input("Your guess was too high! Guess again: "))
            while user < 0 or user > 10:
                user = int(input("Invalid number. Enter a number between 0 an 10: "))
            continue
        elif computer > user:
            user = int(input("Your guess was too low! Guess again: "))
            while user < 0 or user > 10:
                user = int(input("Invalid number. Enter a number between 0 an 10: "))
            continue
    if user == computer:
        print("Your guess was correct! Nice job!")
    print("The random number was " + str(computer) + ".")


evaluate_result()