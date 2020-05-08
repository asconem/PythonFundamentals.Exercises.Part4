user_number = int(input("Pick a number zero or greater: "))
while user_number < 0:
    user_number = int(input("NO NEGATIVES! Pick again: "))


def fibonacci(num):
    a = 0
    b = 1
    if num == 0:
        return a
    elif num == 1:
        return b
    else:
        for i in range(2, num + 1):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(user_number))
