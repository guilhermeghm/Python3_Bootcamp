player1 = input("Player 1: rock, paper, or scissors: ")
player2 = input("Player 2: rock, paper, or scissors: ")

if player1 == player2:
    print("Draw")
elif player1 == "rock" and player2 == "scissors":
    print("Player1 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player1 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player1 wins!")
else:
    print("Player2 wins!")
