//BRUTE-FORCE

import numpy as np

def initialize_move_table():
    move_table = np.zeros((3 ** 9, 9), dtype=int)
    for i in range(3 ** 9):
        ternary = convert_to_ternary(i)
        move_table[i] = ternary
    return move_table

def convert_to_ternary(decimal):
    ternary = np.zeros(9, dtype=int)
    for i in range(8, -1, -1):
        ternary[i] = decimal % 3
        decimal //= 3
    return ternary

def convert_to_decimal(ternary):
    decimal = 0
    for i in range(9):
        decimal = decimal * 3 + ternary[i]
    return decimal

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            index = i * 3 + j
            symbol = 'X' if board[index] == 1 else ('O' if board[index] == 2 else ' ')
            print(symbol, "|", end=" ")
        print()
        print("-------------")

def is_valid_move(board, row, col):
    index = row * 3 + col
    return board[index] == 0

def player_move(board):
    while True:
        print("Enter your move (row and column, separated by space): ")
        row, col = map(int, input().split())
        row -= 1
        col -= 1
        if is_valid_move(board, row, col):
            index = row * 3 + col
            board[index] = 1  # Player move ('X')
            break

def computer_move(board):
    decimal = convert_to_decimal(board)
    move_vector = move_table[decimal]

    for i in range(9):
        if move_vector[i] == 0:
            board[i] = 2  # Computer move ('O')
            return

def is_game_over(board):
    return check_win(board, 1) or check_win(board, 2) or is_board_full(board)

def check_win(board, symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i * 3] == symbol and board[i * 3 + 1] == symbol and board[i * 3 + 2] == symbol) or \
                (board[i] == symbol and board[i + 3] == symbol and board[i + 6] == symbol):
            return True

    if (board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
            (board[2] == symbol and board[4] == symbol and board[6] == symbol):
        return True

    return False

def is_board_full(board):
    return all(cell != 0 for cell in board)

# Main game logic
move_table = initialize_move_table()
board = np.zeros(9, dtype=int)
current_player = 1  # Player always plays as 'X'

while not is_game_over(board):
    print_board(board)

    if current_player == 1:
        player_move(board)
    else:
        computer_move(board)

    current_player = 3 - current_player  # Switch player (1 to 2 or 2 to 1)

print_board(board)
if check_win(board, 1):
    print("Congratulations! You win!")
elif check_win(board, 2):
    print("Computer wins! Better luck next time.")
else:
    print("It's a draw! The game is over.")



//HUERISTIC-APPRAOCH

import numpy as np

def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            row -= 1
            col -= 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")

def heuristic_move(board):
    best_move = find_best_move(board, 'O')
    board[best_move[0]][best_move[1]] = 'O'

def is_game_over(board):
    return get_winner(board) != ' ' or is_board_full(board)

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return ' '  # No winner yet

def find_best_move(board, player):
    best_move = (-1, -1)
    best_score = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def minimax(board, depth, is_maximizing):
    winner = get_winner(board)

    if winner != ' ':
        return 1 if winner == 'O' else -1

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo the move
                    best_score = min(score, best_score)
        return best_score

# Main game logic
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

while not is_game_over(board):
    print_board(board)

    if current_player == 'X':
        player_move(board)
    else:
        heuristic_move(board)

    current_player = 'O' if current_player == 'X' else 'X'

print_board(board)
winner = get_winner(board)
if winner == ' ':
    print("It's a draw!")
else:
    print("Player", winner, "wins!")



//MAGIC-SQUARE

import random

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    def print_board():
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()

    def get_number():
        while True:
            number = input()
            try:
                number = int(number)
                if number in range(1, 10):
                    return number
                else:
                    print("\nNumber not on board")
            except ValueError:
                print("\nThat's not a number. Try again")
                continue

    def turn(player):
        if player == "X":
            placing_index = get_number() - 1
            if board[placing_index] == "X" or board[placing_index] == "O":
                print("\nBox already occupied. Try another one")
                turn(player)
            else:
                board[placing_index] = player
        else:
            # Modified AI strategy to prioritize winning or blocking player
            for i, mark in enumerate(board):
                if mark != 'X' and mark != 'O':
                    board[i] = player
                    if check_win(player):
                        return
                    else:
                        board[i] = mark

            # If no winning move is available, choose a random move
            placing_index = random.choice([i for i, mark in enumerate(board) if mark != 'X' and mark != 'O'])
            board[placing_index] = player

    def check_win(player):
        count = 0
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if board[x] == player and board[y] == player and board[z] == player:
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                print("Player", player, "wins!\n")
                                return True

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while True:
        print_board()
        print("Choose a box player X")
        turn("X")

        print_board()
        if check_win("X"):
            break

        print("AI is making a move...")
        turn("O")

tic_tac_toe()





