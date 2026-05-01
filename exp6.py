import random

board = [' ' for _ in range(9)]

wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_board():
    print(f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]}
""")

def check_winner(player):
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def find_winning_move(player):
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_winner(player):
                board[i] = ' '
                return i
            board[i] = ' '
    return -1

def get_computer_move():
    win_move = find_winning_move('O')
    if win_move != -1:
        return win_move

    block_move = find_winning_move('X')
    if block_move != -1:
        return block_move

    available = [i for i in range(9) if board[i] == ' ']
    return random.choice(available)

def play_game():
    print("Positions: 0-8")
    print_board()

    while True:
        try:
            move = int(input("Your move (0-8): "))
        except:
            print("Invalid input! Enter number.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = 'X'
        print_board()

        if check_winner('X'):
            print("User Wins!")
            break

        if is_draw():
            print("Draw Game!")
            break

        comp_move = get_computer_move()
        board[comp_move] = 'O'
        print(f"Computer chooses: {comp_move}")
        print_board()

        if check_winner('O'):
            print("Computer Wins!")
            break

        if is_draw():
            print("Draw Game!")
            break

play_game()