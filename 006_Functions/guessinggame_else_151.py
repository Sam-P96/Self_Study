import random


def get_int(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f" {temp} is not a valid number") #This will do the same thing as else:


help(get_int)
highest = 1000
answer = random.randint(1, highest)
guess = 0
print(answer)
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_int("") # The input is entered after this str

    if guess == answer:
        print("Well done, you guessed it!")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        if guess == answer:
            print("Well done, you guessed it!")