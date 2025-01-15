#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No winner yet

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None

    while winner is None:
        print_board(board)
        row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner is None:  # If no winner, swap player
                player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print(f"Player {winner} wins!")

tic_tac_toe()
