# Snake Water Gun Game
# Author: Beginner-Friendly Version

# Import random module to allow computer to choose randomly
import random

# Create a list of possible choices
game_choices = ["snake", "water", "gun"]

# Computer randomly selects one choice from the list
computer = random.choice(game_choices)

# Take input from the user
user = input("Enter Snake, Water, or Gun: ").lower()

# Display choices
print("\nYou chose:", user)
print("Computer chose:", computer)

# Check if user entered a valid choice
if user not in game_choices:
    print("\nInvalid input! Please enter Snake, Water, or Gun.")

# If both choices are the same
elif user == computer:
    print("\nIt's a Draw!")

# User chooses snake
elif user == "snake":
    if computer == "water":
        print("\nSnake drinks Water.")
        print("You Win!")
    else:  # computer == gun
        print("\nGun kills Snake.")
        print("Computer Wins!")

# User chooses water
elif user == "water":
    if computer == "gun":
        print("\nWater damages Gun.")
        print("You Win!")
    else:  # computer == snake
        print("\nSnake drinks Water.")
        print("Computer Wins!")

# User chooses gun
elif user == "gun":
    if computer == "snake":
        print("\nGun kills Snake.")
        print("You Win!")
    else:  # computer == water
        print("\nWater damages Gun.")
        print("Computer Wins!")