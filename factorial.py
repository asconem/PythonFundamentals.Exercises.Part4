def factorial():
    user_input = int(input("Please enter a number from zero to 994: "))
    while user_input < 0 or user_input > 994:
        user_input = int(input("Invalid entry. Please enter a number from zero to 994: "))

    num = 1
    if user_input >= 1:
        for i in range(1, user_input + 1):
            num = num * i
    print(num)


factorial()