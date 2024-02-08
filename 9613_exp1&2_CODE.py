#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Brute Force Approach 


# In[1]:


import random

board = [' ' for x in range(9)]
def main():
    print('Game started')
    print_board()
    game_end = False
    while not game_end:
        print('Player turn')
        player_turn()
        print_board()
        if check_winner(board):
            print('Player won')
            game_end = True
            break

        print('Computer turn')
        computer_move = computer_turn()
        if computer_move != -1:
            board[computer_move] = 'O'
            print_board()
            if check_winner(board):
                print('Computer won')
                game_end = True
                break

        if board.count(' ') < 1:
            print('Tie game')
            game_end = True

    print('Game ended')

def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_winner(board):
    if ((board[0] == board[1] == board[2] != ' ') or
        (board[3] == board[4] == board[5] != ' ') or
        (board[6] == board[7] == board[8] != ' ')):
        return True

    if ((board[0] == board[3] == board[6] != ' ') or
        (board[1] == board[4] == board[7] != ' ') or
        (board[2] == board[5] == board[8] != ' ')):
        return True

    if ((board[0] == board[4] == board[8] != ' ') or
        (board[2] == board[4] == board[6] != ' ')):
        return True

    return False

def player_turn():
    made_move = False
    while not made_move:
        player_input = input('Enter a position (1-9) ')
        try:
            player_move = int(player_input)
            if player_move < 1 or player_move > 9:
                print('Enter a valid position')
            else:
                player_position = player_move - 1 # player index in board
                if board[player_position] != ' ':
                    print('Position is already taken')
                else:
                    board[player_position] = 'X'
                    made_move = True

        except:
            print('Enter a valid number')


def computer_turn():

    available_moves = [pos for pos, value in enumerate(board) if value == ' ']

    move = -1



    for i in available_moves:
        new_board = board[:]
        new_board[i] = 'O'
        if check_winner(new_board):
            move = i
            return move

    for i in available_moves:
        new_board = board[:]
        new_board[i] = 'X'
        if check_winner(new_board):
            move = i
            return move

    avalable_corners = []
    for i in available_moves:
        if i in [0, 2, 6, 8]:
            avalable_corners.append(i)

    if len(avalable_corners) > 0:
        random_index = random.randrange(0, len(avalable_corners))
        move = avalable_corners[random_index]
        return move

    if 4 in available_moves:
        move = 4
        return move

    avalable_edges = []
    for i in available_moves:
        if i in [1, 3, 5, 7]:
            avalable_edges.append(i)

    if len(avalable_edges) > 0:
        random_index = random.randrange(0, len(avalable_edges))
        move = avalable_edges[random_index]
        return move

    return move
    
if __name__ == '__main__':

    main()


# In[ ]:


Heuristic Approach


# In[14]:


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' 
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # Empty line

            if game.current_winner:
                if print_game:
                    if game.current_winner == 'O':
                        print('Computer wins!')
                    else:
                        print(letter + ' wins!')
                return game.current_winner  

            letter = 'O' if letter == 'X' else 'X'  

        if print_game:
            print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


# Magic Square method 

# In[3]:


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_computer_move(board, player_symbol, computer_symbol):
    magic_square = [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]
    ]

    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    for i, j in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[i][j] = computer_symbol
        if is_winner(temp_board, computer_symbol):
            return i * 3 + j + 1

    for i, j in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[i][j] = player_symbol
        if is_winner(temp_board, player_symbol):
            return i * 3 + j + 1

    return random.choice(empty_cells)[0] * 3 + random.choice(empty_cells)[1] + 1

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_symbol, computer_symbol = 'X', 'O'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for move_num in range(1, 10):
        current_player = user_symbol if move_num % 2 == 1 else computer_symbol

        if current_player == user_symbol:
            user_move = get_user_move()
            row, col = divmod(user_move - 1, 3)
        else:
            computer_move = calculate_computer_move(board, user_symbol, computer_symbol)
            row, col = divmod(computer_move - 1, 3)
            print(f"Computer chooses position {computer_move}")

        while board[row][col] != ' ':
            print("ERROR! That position is already taken. Choose a different one.")
            if current_player == user_symbol:
                user_move = get_user_move()
                row, col = divmod(user_move - 1, 3)
            else:
                computer_move = calculate_computer_move(board, user_symbol, computer_symbol)
                row, col = divmod(computer_move - 1, 3)

        board[row][col] = user_symbol if current_player == user_symbol else computer_symbol
        print_board(board)

        if is_winner(board, current_player):
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()


# In[ ]:




