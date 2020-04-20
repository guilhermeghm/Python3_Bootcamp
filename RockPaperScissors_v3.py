#Import the module
from random import randint

#Print something to start.
print("Rock...")
print("Paper...")
print("Scissors...")

#User define his option.
player = input("Player, make your move: ").lower()

#Computer define his option.
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

#Logic to validate both values.
if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
else:
    print("Please enter a valid move!")
