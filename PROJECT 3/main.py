# Number Guessing Game
def game():
    # Making choice
    import random
    number=random.randint(1,100)

    while True:
        # Guessing
        guess=int(input("Enter your guess:"))

        if(number>guess):
            print("You need to go Higher!")
        elif(number<guess):
            print("You need to go Lower!")
        else:
            print("You Won!!")
            break
game()

