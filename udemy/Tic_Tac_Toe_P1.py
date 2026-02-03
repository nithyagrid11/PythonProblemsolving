import random

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9]) #dynamic entry in which, is used for later entries using index value
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
#to show the board values
#display_board(test_board)

def player_input():
    marker = ''
    while marker not in ['X','O']:
        marker = input('Player 1: Do you want to be "X" or "O"? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
#xPlayer1_marker, Player2_marker = player_input()
#print(Player1_marker, Player2_marker)

def place_marker(board,marker,position):
    board[position] = marker
#place_marker(test_board,'O',5)
#display_board(test_board)

def win_check(board,mark):
    win_combinations = [
        (7,8,9),
        (4,5,6),
        (1,2,3),
        (7,5,3),
        (1,5,9),
        (7,4,1),
        (8,5,2),
        (9,6,3)
    ]
    for a,b,c in win_combinations:
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
    return False
#print(win_check(test_board,'O'))

def choose_first():
    player1 = 0
    player2 = 1
    choose = random.randint(player1,player2)
    if choose == 0:
        return 'Player 1'
    else:
        return 'Player 2'
#print(choose_first())

def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False
#print(space_check(test_board,1))

def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True
#print(full_board_check(test_board))

def player_choice(board):
    position = int(input('Select next position: '))
    while not space_check(board,position):
        position = int(input('That position is not free. Choose again: '))
    return position
#print(player_choice(test_board))

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
#print(replay())

print('Welcome to Tic Tac Toe Game!!!')
while True:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(test_board)
    
    Player1_marker, Player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    game_on = True
    while game_on:
        if turn == 'Player 1':
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,Player1_marker,position)

            if win_check(test_board,Player1_marker):
                display_board(test_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('Draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,Player2_marker,position)

            if win_check(test_board,Player2_marker):
                display_board(test_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('Draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
