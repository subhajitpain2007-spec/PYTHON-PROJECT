'''We all have played snake, water gun game in our childhood. If you haven't, google the
rules of this game and write a python program capable of playing this game with the
user.'''
import random

choices = ["snake", "water", "gun"]

user = input("Enter snake, water or gun: ").lower()
computer = random.choice(choices)

print("You:", user)
print("Computer:", computer)

if user == computer:
    print("Draw!")

elif (
    (user == "snake" and computer == "water") or
    (user == "water" and computer == "gun") or
    (user == "gun" and computer == "snake")
):
    print("You Win!")

else:
    print("Computer Wins!")