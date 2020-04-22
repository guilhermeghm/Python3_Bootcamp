#Import the module
from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    #Print something to start.
    print(f"Player Score: {player_wins} Computer Score {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    #User define his option.
    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break

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
        print("It's a tie! \n")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins! \n")
            player_wins +=1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!\n")
            player_wins +=1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!\n")
            player_wins +=1
        else:
            print("Computer wins!\n")
            computer_wins += 1
    else:
        print("Please enter a valid move!\n")

if player_wins > computer_wins:
    print("Congrats, you won!\n")
elif player_wins == computer_wins:
    print("It's a tie!\n")
else:
    print("Oh no :( The computer won...\n")

print("Final Score: ")
print(f"Player Score: {player_wins} Computer Score {computer_wins}")
