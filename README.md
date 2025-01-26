# gobble_mania
 Gobble is a Python-based 3x3 grid game where players strategically place size-priority pieces (Large > Medium > Small) to align three in a row and win.


# How to Play
Players take turns to place a piece on a 3x3 grid.
Each piece has a size:
L: Large
M: Medium
S: Small
Larger pieces can replace smaller pieces already on the grid.
The objective: Align three pieces of the same player (row, column, or diagonal) to win!
Controls:

Input the row (0–2) and column (0–2) to place your piece.
Choose the size of the piece (L, M, S)

# Features
Size-based Priority Mechanics: Larger pieces can replace smaller ones, making each turn a tactical decision.
Dynamic Winner Detection: Real-time checking for rows, columns, and diagonals.
Error Validation: Prevents invalid moves like stacking equal or smaller-sized pieces.
Console-based Interface: Simple and clean terminal gameplay.

# Tech Stack
Language: Python
Library: NumPy (for efficient grid management)


Thanks to classic grid-based games like Tic-Tac-Toe for inspiring the mechanics of Gobble. This project was built as a fun way to explore game development logic, strategic thinking, and Python programming.
