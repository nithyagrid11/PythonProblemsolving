import random

def display_board(board):
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    print('Tic-Tac-Toe Game Starts!')
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    if marker == 'O':
        return ('O', 'X')
print(player_input())

def place_marker(board,marker,position):
    board[position] = marker
place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, mark):
    win_combinations = [
        [7, 8, 9],  # top row
        [4, 5, 6],  # middle row
        [1, 2, 3],  # bottom row
        [7, 4, 1],  # left column
        [8, 5, 2],  # middle column
        [9, 6, 3],  # right column
        [7, 5, 3],  # diagonal
        [9, 5, 1]   # diagonal
    ]
    for combo in win_combinations:
        if board[combo[0]] == mark and board[combo[1]] == mark and board[combo[2]] == mark:
            return True
    return False
print(win_check(test_board,'X'))

def choose_first():
    player_1 = 0
    player_2 = 1
    first = random.randint(player_1, player_2)
    if first == 0:
        return 'Player 1'
    else:
        return 'Player 2'
print(choose_first())

def space_check(board, position):
    if board[position] == ' ':
        return True
    return False
print(space_check(test_board,2))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
print(full_board_check(test_board))

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
player_choice(test_board)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')