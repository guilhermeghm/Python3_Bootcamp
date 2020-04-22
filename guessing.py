#handle user guesses
#   if they guess correct, tell them they won
#    otherwise tell them if they are too high or too low.

# Bonus - let player play again if they want!

import random

random_number = random.randint(1,10) #numbers 1 - 10
guess = None

while guess != random_number:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too Low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("You Won!!!!")

print(random_number)
