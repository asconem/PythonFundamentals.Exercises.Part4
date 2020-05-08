user_number = int(input("Pick a number between 1 and 30: "))
while user_number < 1 or user_number > 30:
    user_number = int(input("Invalid selection. Pick a number between 1 and 30: "))


def fib_sequence(num):
    if num <= 1:
        return num
    else:
        return fib_sequence(num - 1) + fib_sequence(num - 2)


print(fib_sequence(user_number))
