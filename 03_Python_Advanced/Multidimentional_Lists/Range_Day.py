import sys
from io import StringIO

test_input_1 = """. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right
"""
#sys.stdin = StringIO(test_input_1)

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def find_position(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol:
                return row, col
    return -1, -1

def move(direction, steps, row, col, matrix):
    if direction == "up":
        for _ in range(steps):
            row -= 1
            if row < 0 or matrix[row][col] != ".":
                return row + 1, col
    elif direction == "down":
        for _ in range(steps):
            row += 1
            if row >= len(matrix) or matrix[row][col] != ".":
                return row - 1, col
    elif direction == "left":
        for _ in range(steps):
            col -= 1
            if col < 0 or matrix[row][col] != ".":
                return row, col + 1
    elif direction == "right":
        for _ in range(steps):
            col += 1
            if col >= len(matrix[0]) or matrix[row][col] != ".":
                return row, col - 1
    return row, col

def shoot(direction, row, col, matrix):
    if direction == "up":
        for r in range(row - 1, -1, -1):
            if matrix[r][col] == "x":
                matrix[r][col] = "."
                return [r, col]
    elif direction == "down":
        for r in range(row + 1, len(matrix)):
            if matrix[r][col] == "x":
                matrix[r][col] = "."
                return [r, col]
    elif direction == "left":
        for c in range(col - 1, -1, -1):
            if matrix[row][c] == "x":
                matrix[row][c] = "."
                return [row, c]
    elif direction == "right":
        for c in range(col + 1, len(matrix[0])):
            if matrix[row][c] == "x":
                matrix[row][c] = "."
                return [row, c]
    return None

# Input parsing
matrix = []
for _ in range(5):
    matrix.append(input().split())

n = int(input())

row, col = find_position(matrix, "A")

hit_targets = []

# Process commands
for _ in range(n):
    command_args = input().split()
    command = command_args[0]
    if command == "move":
        direction = command_args[1]
        steps = int(command_args[2])
        row, col = move(direction, steps, row, col, matrix)
    elif command == "shoot":
        direction = command_args[1]
        hit_position = shoot(direction, row, col, matrix)
        if hit_position:
            hit_targets.append(hit_position)

total_targets = sum(row.count("x") for row in matrix)
if total_targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

for target in hit_targets:
    print(f"[{target[0]}, {target[1]}]")
