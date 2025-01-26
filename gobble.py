import numpy as np

board = np.empty((3, 3), dtype=object)
for i in range(3):
    for j in range(3):
        board[i, j] = None

def print_grid(grid):
    print("\n  0     1     2")
    for i, row in enumerate(grid):
        row_str = " | ".join([" " if cell is None else f"{cell[0]}({cell[1]})" for cell in row])
        print(f"{i} {row_str}")
        if i < 2:
            print("  " + "-" * 17)
    print()

print("Welcome to Gobble! The game is played on a 3x3 grid.")
print("Players take turns placing pieces (Large=L, Medium=M, Small=S).")
print("The objective is to align 3 pieces in a row, column, or diagonal.")
print("Pieces of higher priority replace smaller ones. Let's begin!\n")

turn_number = 1
game_over = False

def get_current_player(turn_number):
    return "P1" if turn_number % 2 == 1 else "P2"

def place_piece(board, row, col, player, size):
    size_order = {'L': 3, 'M': 2, 'S': 1}
    current_cell = board[row, col]

    if current_cell:
        existing_player, existing_size = current_cell
        existing_size_priority = size_order.get(existing_size)
        new_size_priority = size_order.get(size)
        if new_size_priority <= existing_size_priority:
            print("Invalid move! Cannot replace or stack a piece of equal or smaller priority.")
            return False

    board[row, col] = (player, size)
    return True

def check_winner(board):
    for i in range(3):
        if check_line(board[i, :]) or check_line(board[:, i]):
            return True
    diagonal1 = [board[i, i] for i in range(3)]
    diagonal2 = [board[i, 2 - i] for i in range(3)]
    if check_line(diagonal1) or check_line(diagonal2):
        return True
    return False

def check_line(line):
    if all(cell is not None for cell in line):
        top_players = [cell[0] for cell in line]
        if all(top_players[0] == player for player in top_players):
            return True
    return False

while not game_over:
    print_grid(board)
    player = get_current_player(turn_number)
    print(f"Player {player}'s turn.")
    
    try:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid input! Row and column must be between 0 and 2.")
            continue
    except ValueError:
        print("Invalid input! Please enter numbers between 0 and 2.")
        continue

    size = input("Choose piece size (L for Large, M for Medium, S for Small): ").upper()
    if size not in ['L', 'M', 'S']:
        print("Invalid size. Please choose L, M, or S.")
        continue

    if place_piece(board, row, col, player, size):
        print("Piece placed successfully!")
    else:
        print("Try again with a valid move.")
        continue

    if check_winner(board):
        print_grid(board)
        print(f"\nPlayer {player} wins!")
        game_over = True
        break

    if all(board[row, col] is not None for row in range(3) for col in range(3)):
        print_grid(board)
        print("\nIt's a draw!")
        game_over = True
        break

    turn_number += 1
