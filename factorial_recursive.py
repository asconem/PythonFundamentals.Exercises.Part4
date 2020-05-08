user_input = int(input("Please enter a number from 0 to 994: "))
while user_input < 0 or user_input > 994:
    user_input = int(input("Invalid entry. Please enter a number from 0 to 994: "))


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(user_input))