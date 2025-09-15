import sys
from io import StringIO

test_input_1 = """7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
"""
#sys.stdin = StringIO(test_input_1)

def find_allice(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "A":
                return (row, col)

def is_valid(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    return True

n = int(input())

matrix = []

for i in range(n):
    matrix.append(input().split())

allice_coordinates = find_allice(matrix)

row = allice_coordinates[0]
col = allice_coordinates[1]
matrix[row][col] = "*"

counter = 0

is_out = False
while True:

    if counter >= 10:
        is_out = False
        break

    command = input()
    if command == "up":
        row -= 1
        if is_valid(row, col, matrix):
            if matrix[row][col] == "R":
                matrix[row][col] = "*"
                is_out = True
                break
            if matrix[row][col].isdigit():
                counter += int(matrix[row][col])
            matrix[row][col] = "*"
        else:
            is_out = True

    elif command == "down":
        row += 1
        if is_valid(row, col, matrix):
            if matrix[row][col] == "R":
                matrix[row][col] = "*"
                is_out = True
                break
            if matrix[row][col].isdigit():
                counter += int(matrix[row][col])
            matrix[row][col] = "*"
        else:
            is_out = True

    elif command == "left":
        col -= 1
        if is_valid(row, col, matrix):
            if matrix[row][col] == "R":
                is_out = True
                matrix[row][col] = "*"
                break
            if matrix[row][col].isdigit():
                counter += int(matrix[row][col])
            matrix[row][col] = "*"
        else:
            is_out = True

    else: #right
        col += 1
        if is_valid(row, col, matrix):
            if matrix[row][col] == "R":
                matrix[row][col] = "*"
                is_out = True
                break
            if matrix[row][col].isdigit():
                counter += int(matrix[row][col])
            matrix[row][col] = "*"
        else:
            is_out = True



if is_out:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)