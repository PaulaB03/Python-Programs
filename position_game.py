import os
# Funtion to clear the historical output
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Variable that keeps the game on
game_on = True

# initial list
game_list = [0,1 ,2, 3, 4]

# Function to displat the current list
def display_game(game_list):
    print("Here is the current list")
    print(game_list)


# Function that returns the position we want to switch
def position_choise():
    choise = 'wrong'

    # Reads while we get a valid integer
    while not choise.isdigit():
        # reads the input
        choise = input(f"Pick a position between 0 and {len(game_list)-1} to replace: ")

        # if the input is not valid
        if not choise.isdigit():
            print("Please pick a number")
        elif int(choise) not in range(0,len(game_list)):
            choise = 'wrong'
            print("Sorry, but you did not choose a valid position")

    clear()
    return int(choise)


# Function that replace the curent position's string
def replacement_choise(game_list, position):
    replacement = input("Type a new string to place at the position: ")
    game_list[position] = replacement

    return  game_list


# Function to stop/continue game
def game_on_choise():
    choise = 'wrong'

    while choise not in ['Y', 'y', 'n', 'N']:
        choise = input("Would you like to continue playing the game? Y or N ")

        # Checks if the input is valid
        if choise not in ['Y', 'y', 'n', 'N']:
            print("Sorry, I didn't understand.")

    clear()
    if choise in ['Y', 'y']: return True
    else: return False


# Function to choose an option
def option_choise():
    # Tha game options
    print("Pick an option")
    print("1 - Replace a value from a position")
    print("2 - Add a new position")
    print("3 - Remove a certain position")
    print("4 - Display the current list")
    print("0 - Exit program")

    choise = 'wrong'

    while choise not in ['1', '2', '3','4', '0']:
        choise = input("Your option : ")

        # if the input is not valid
        if choise not in ['1', '2', '3','4', '0']:
            print("Please pick a valid number")

    return int(choise)


# The actual game
while game_on:
    # Pick an option
    clear()
    option = option_choise()

    # Clears the historical output and display the current list
    clear()
    display_game(game_list)

    match option:
        case 1:
            print("Replace a value from a position")

            # Pick a position
            position = position_choise()

            # Rewrite that position
            game_list = replacement_choise(game_list, position)

        case 2:
            print("Add a new position")

            # Add a new position at the end of the list
            str = input('Type a string for the new position: ')
            game_list.append(str)

        case 3:
            print("Remove a certain position")

            # Pick a position and removes that position
            position = position_choise()
            game_list.pop(position)

        case 4:
            print("Display the current list")
            
            clear()
            display_game(game_list)

        case 0:
            break

    # Clear Screen and show the updated list
    clear()
    display_game(game_list)

    # Wanna continue?
    game_on = game_on_choise()

clear()
print("Good bye")