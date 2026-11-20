
import random

print("=================================")
print("     WELCOME TO NUMBER GUESSING")
print("=================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif guess < secret_number:
            print("Too low! Try a bigger number.")

        elif guess > secret_number:
            print("Too high! Try a smaller number.")

        else:
            print("\n🎉 Congratulations! You guessed it!")
            print("The correct number was:", secret_number)
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\nThanks for playing!")
