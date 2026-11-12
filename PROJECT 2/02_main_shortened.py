# Rock, Paper, Scissors Game
# This program lets the user play against the computer.

import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Computer randomly selects a choice
computer = random.choice(choices)

# Get user's choice
user = input("Enter rock, paper, or scissors: ").lower()

# Check if the user's input is valid
if user not in choices:
    print("Invalid choice! Please run the program again.")
else:
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    # Determine the winner
    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")