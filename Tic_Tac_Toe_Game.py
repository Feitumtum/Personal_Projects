# Tic Tac Toe Game
# By: Crystal Lin
#======================================================================

# imports
from IPython.display import clear_output
clear_output()


# ---------------------------------------------------------------------
# Defining Functions for Game
# ---------------------------------------------------------------------

def board_ref():
    print('1|2|3')
    print('-----')
    print('4|5|6')
    print('-----')
    print('7|8|9 \n')

def print_board(positions): # Function to print whole board given the 3 rows

    global f1, f2, f3
    [holder,s1,s2,s3,s4,s5,s6,s7,s8,s9] = positions

    r1 = ('{}|{}|{}'.format(s1,s2,s3))
    f1 = '-----'
    r2 = ('{}|{}|{}'.format(s4,s5,s6))
    f2 = '-----'
    r3 = ('{}|{}|{}\n'.format(s7,s8,s9))
    f3 = '-----'

    print('Current Board')
    print(r1)
    print(f1)
    print(r2)
    print(f2)
    print(r3)

def game_reset(): # Function to reset board to empty

    global f1, f2, f3

    [holder,s1,s2,s3,s4,s5,s6,s7,s8,s9] = ori_board

    print('\nNew Game!')
    board_ref()
    print_board(ori_board)

# function should take user input for game or not, and return True/False UNFINSIHED!!!!!
def start_game():

    choice = 'input' # initalize var
    check = False # test if input is valid

    options = ['Yes', 'No'] # only choices/validation

    while choice not in options:
        clear_output()
        choice = input('Do you want to play Tic Tac Toe?')
        print('Need to either put in "Yes" or "No"')


    if choice == 'Yes':
        return True # return True to start game
    else:
        print('Let me know when you want to play again!')
        return False

def one_move_each(player,current_board):
    choice = 'input'
    valid = False
    in_range = False
    open_space = False

    # input must meet three criteria to be usable input
    while valid == False or in_range == False or open_space == False:

        # Input prompt based on player
        if player == 1:
            choice = input('Player 1 (x) choose a #: ')
        elif player == 2:
            choice = input('Player 2 (o) choose a #: ')

        # Checks if input is a digit
        if  choice.isdigit() == False:
            clear_output()
            print('Please choose a digit/number')
            valid = False
        else:
            valid = True

        # Checks if within board positions
        choice = int(choice)
        if choice not in range(1,10):
            clear_output()
            print('Please choose a number from 1 to 9!')
            in_range = False
            continue
        else:
            in_range = True

        if current_board[choice] != ' ':
            clear_output()
            print('Please choose an open space!')
            board_ref()
            print_board(current_board)
            open_space = False
        else:
            open_space = True

    # x or o based on player
    if player == 1:
        current_board[choice] = 'x'
    elif player == 2:
        current_board[choice] = 'o'

    print_board(current_board) # prints so users can see new board
    return current_board # returns board so we can store it

def win_check(current_board): # returns boolean to indicate if one person has won
    s = current_board
    array_board = [s[1:4], s[4:7], s[7:10]]

    win_cond1 = 3*['x']
    win_cond2 = 3*['o']
    winner = 'none'

    # checking for 3 in a row
    for i in range(0,3):
        check = []
        for j in range(0,3):
            check.append(array_board[i][j])

        if check == win_cond1:
            winner = 'Player 1'
            return [winner,True]
        elif check == win_cond2:
            winner = 'Player 2'
            return [winner,True]


    # checking for 3 in a column
    for j in range(0,3):
        check = []
        for i in range(0,3):
            check.append(array_board[i][j])

        if check == win_cond1:
            winner = 'Player 1'
            return [winner,True]
        elif check == win_cond2:
            winner = 'Player 2'
            return [winner,True]

    # checking left to right diagonal
    if array_board[0][0] == array_board[1][1] and array_board[1][1] == array_board[2][2] and array_board[0][0] != ' ':
        if array_board[0][0] == 'x':
            winner = 'Player 1'
            return [winner,True]
        else:
            winner = 'Player 2'
            return [winner,True]

    # checking right to left diagonal
    elif array_board[2][0] == array_board[1][1] and array_board[2][0] == array_board[0][2] and array_board[2][0] != ' ':
        if array_board[2][0] == 'x':
            winner = 'Player 1'
            return [winner,True]
        else:
            winner = 'Player 2'
            return [winner,True]


    return [winner, False]

def cont_game():

    choice = 'none'

    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:

        choice = input("Play Again? Y or N: ")

        if choice not in ['Y','N']:
            clear_output()
            print("Make sure to choose Y or N.")

    if choice == "Y":
        return True
    else:
        return False

# =====================================================================
# Begining of the whole game
# =====================================================================
game_on = True


while game_on:
    win = False
    board_ref
    ori_board = ['Empty',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    current_board = ori_board
    game_reset()

    while win == False:

        # Player 1 moves
        current_board = one_move_each(1,current_board)
        if win_check(current_board)[1] == True:
            print(f'The winner is {win_check(current_board)[0]} !')
            win = True

        # Check if Win
        if win == True:
            break

        # Check if Tie
        spaces_filled = 0
        for i in range(1,10):
            spaces_filled = spaces_filled + (current_board[i] != ' ')

        if spaces_filled == 9:
            print('Its a Tie!')
            break

        # Player 2 moves
        current_board = one_move_each(2,current_board)
        if win_check(current_board)[1] == True:
            print(f'The winner is {win_check(current_board)[0]} !')
            win = True

    game_on = cont_game()

print('\nAwww ok...Bye!')
