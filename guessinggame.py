import random

highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it!")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        if guess == answer:
            print("Well done, you guessed it!")