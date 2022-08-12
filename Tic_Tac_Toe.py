import os
# Funtion to clear the historical output
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Function to stop/restart the game
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


# Function that prints the board
def display_bord(board):
    print("Current board")
    print(f' {board[0]}  |  {board[1]}  |  {board[2]}')
    print("- - - - - - - - ")
    print(f' {board[3]}  |  {board[4]}  |  {board[5]}')
    print("- - - - - - - - ")
    print(f' {board[6]}  |  {board[7]}  |  {board[8]}')
    print('\n')


# Function to make a move on the board
def input_position(turn):
    print("Position index")
    print(" 0 | 1 | 2")
    print(" - - - - - ")
    print(" 3 | 4 | 5")
    print(" - - - - - ")
    print(" 6 | 7 | 8\n")
    print(f"It's {player[turn%2]} turn")

    position = 'wrong'

    while position not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        position = input("Please pick your next move: ")

        if position not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print("Please pick a valid option")
        elif board[int(position)] != ' ':
            position = 'wrong'
            print("That position is already taken")
        else:
            board[int(position)] = player[turn%2]

    return board


# Function to check if the game is over
def end_game():
    # Check if there is a winner on the diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return (False, board[0])
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return (False, board[2])

    for i in range(0,3):
        # Check if there is a winner on the rows
        if board[3*i] == board[3*i+1] == board[3*i+2] and board[3*i] != ' ':
            return (False, board[3*i])

        #Check if there is a winner on the columns
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return (False, board[i])

        #Check if there are no positions left
        if ' ' not in board:
            return (False, ' ')

    return (True, ' ')

def tic_tac_toe(board, turn):
    # Variable that keeps the round on
    round_on = True
    winner = ' '

    while round_on:
        clear()
        display_bord(board)
        board = input_position(turn)
        turn += 1
        (round_on, winner) = end_game()

    clear()
    display_bord(board)
    if winner != ' ':
        print(f'{winner} won')
        if(winner == 'X'): score[0] += 1
        else: score[1] += 1
    else:
        print("Draw")

    print_score()

def print_score():
    print("Current score")
    print(f'{player[0]}: {score[0]}\n{player[1]}: {score[1]}')
    print('\n')


# Variable that keeps the game on
game_on = True

# Variable to keep track of the game
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Variable for number of turn, players and score
turn = 0
player = ['X', 'O']
score = [0, 0]

while game_on:
    tic_tac_toe(board, turn)
    game_on = game_on_choise()

    # Resets the values
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    turn = 0

print("Final score")
print(f'{player[0]}: {score[0]}\n{player[1]}: {score[1]}')
print('The game ended in a draw' if score[0] == score[1] else
      f'{player[0] if score[0]>score[1] else player[1]} won the game')