
import random

# Welcome message
print("======================================")
print("     WELCOME TO ROCK PAPER SCISSORS")
print("======================================")

print("Rules of the Game:")
print("1. Rock beats Scissors")
print("2. Scissors beats Paper")
print("3. Paper beats Rock")
print("4. If both choose the same, it's a Draw!")

# Store all possible choices in a list
choices = ["rock", "paper", "scissors"]

# Ask the player to enter their choice
player = input("\nEnter your choice (rock/paper/scissors): ").lower()

# Check whether the player's choice is valid
if player not in choices:
    print("\nInvalid choice! Please choose rock, paper, or scissors.")

else:

    # Computer randomly selects one option
    computer = random.choice(choices)

    # Display both choices
    print("\n--------------------------------------")
    print("You selected:", player.upper())
    print("Computer selected:", computer.upper())
    print("--------------------------------------")

    # Compare both choices to decide the winner

    if player == computer:

        # Both choices are the same
        print("\nIT'S A DRAW!")
        print("You both selected", player.upper())
        print("Since both choices are identical, nobody wins!")

    elif player == "rock" and computer == "scissors":

        # Rock defeats Scissors
        print("\nCONGRATULATIONS! YOU WON!")
        print("You chose ROCK.")
        print("Computer chose SCISSORS.")
        print("Why did you win?")
        print("Because ROCK beats SCISSORS!")
        print("Your rock crushed the computer's scissors!")

    elif player == "paper" and computer == "rock":

        # Paper defeats Rock
        print("\nCONGRATULATIONS! YOU WON!")
        print("You chose PAPER.")
        print("Computer chose ROCK.")
        print("Why did you win?")
        print("Because PAPER beats ROCK!")
        print("Your paper covered the computer's rock!")

    elif player == "scissors" and computer == "paper":

        # Scissors defeats Paper
        print("\nCONGRATULATIONS! YOU WON!")
        print("You chose SCISSORS.")
        print("Computer chose PAPER.")
        print("Why did you win?")
        print("Because SCISSORS beats PAPER!")
        print("Your scissors cut the computer's paper!")

    else:

        # If none of the above conditions are true,
        # the computer must have won
        print("\nSORRY! YOU LOST!")

        print("You chose:", player.upper())
        print("Computer chose:", computer.upper())

        print("\nWhy did the computer win?")

        # Explain the exact reason for losing
        if computer == "rock":
            print("Computer chose ROCK, which beats SCISSORS!")

        elif computer == "paper":
            print("Computer chose PAPER, which beats ROCK!")

        elif computer == "scissors":
            print("Computer chose SCISSORS, which beats PAPER!")

        print("Better luck next time!")

print("\n======================================")
print("          THANKS FOR PLAYING!")
print("======================================")
