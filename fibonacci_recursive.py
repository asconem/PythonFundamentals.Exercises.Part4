user_number = int(input("Pick a number between 1 and 30: "))
while user_number < 1 or user_number > 30:
    user_number = int(input("Invalid selection. Pick a number between 1 and 30: "))


def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(user_number))
