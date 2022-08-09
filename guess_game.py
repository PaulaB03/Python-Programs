import os
import random
# Funtion to clear the historical output
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Variable that keeps the game on
game_on = True

# Function to stop/continue game
def game_on_choise():
    choise = 'wrong'

    while choise not in ['Y', 'y', 'n', 'N']:
        choise = input("Would you like to replay the game? Y or N ")

        # Checks if the input is valid
        if choise not in ['Y', 'y', 'n', 'N']:
            print("Sorry, I didn't understand.")

    clear()
    if choise in ['Y', 'y']: return True
    else: return False


# Function to read a valid number
def input_number():
    while True:
        guess = input("Your guess: ")

        if guess.isdigit() == False: print("Please write a valid input")
        else:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("OUT OF BOUNDS")
            else:
                break

    return guess


while game_on:
    # Clears the historical output and randomize a number
    clear()
    number = random.randint(1,101)

    # The rules of the game
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!\n")

    guesses = []
    while True:
        guess = input_number()
        guesses.append(guess)

        if guess == number:
            clear()
            print(f'Congratulations, the number was {number}')
            print(f'you guessed it in only {len(guesses)} guesses!')
            break

        if len(guesses) > 1:
            if abs(number-guess) < abs(number-guesses[-2]):
                print("WARMER")
            else:
                print("COLDER")
        else:
            if abs(number-guess) < 10:
                print("WARM")
            else:
                print("COLD")

    game_on = game_on_choise()