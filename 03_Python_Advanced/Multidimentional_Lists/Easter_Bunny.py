import sys
from io import StringIO

test_input_1 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""
#sys.stdin = StringIO(test_input_1)

def find_bunny(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "B":
                return (row, col)

def is_in_matrix(matrix, row, col):
    # Check if row and col are within bounds
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    return True

def find_trap(matrix, row, col):
    if matrix[row][col] == "X":
        return True
    return False

def find_biggest_path(matrix, coordinates):
    biggest_count = 0
    direction = ""
    founded_eggs = []

    row = coordinates[0]
    col = coordinates[1]
    current_count = 0
    collected_eggs = []
    while True: #UP
        row -= 1
        if not is_in_matrix(matrix, row, col):
            break
        else:

            if not find_trap(matrix, row, col):
                current_count += int(matrix[row][col])
                collected_eggs.append([row, col])
                if current_count > biggest_count:
                    biggest_count = current_count
                    direction = "up"
                    founded_eggs = collected_eggs

            else:
                break

    row = coordinates[0]
    col = coordinates[1]
    current_count = 0
    collected_eggs = []
    while True: #down
        row += 1
        if not is_in_matrix(matrix, row, col):
            break
        else:

            if not find_trap(matrix, row, col):
                current_count += int(matrix[row][col])
                collected_eggs.append([row, col])
                if current_count > biggest_count:
                    biggest_count = current_count
                    direction = "down"
                    founded_eggs = collected_eggs

            else:
                break

    row = coordinates[0]
    col = coordinates[1]
    current_count = 0
    collected_eggs = []
    while True: #left
        col -= 1
        if not is_in_matrix(matrix, row, col):
            break
        else:

            if not find_trap(matrix, row, col):
                current_count += int(matrix[row][col])
                collected_eggs.append([row, col])
                if current_count > biggest_count:
                    biggest_count = current_count
                    direction = "left"
                    founded_eggs = collected_eggs

            else:
                break

    row = coordinates[0]
    col = coordinates[1]
    current_count = 0
    collected_eggs = []
    while True: #right
        col += 1
        if not is_in_matrix(matrix, row, col):
            break
        else:

            if not find_trap(matrix, row, col):
                current_count += int(matrix[row][col])
                collected_eggs.append([row, col])
                if current_count > biggest_count:
                    biggest_count = current_count
                    direction = "right"
                    founded_eggs = collected_eggs
            else:
                break

    return biggest_count, direction, founded_eggs





size = int(input())

matrix = []
for row in range(size):
    matrix.append(input(). split())

bunny_coordinates = find_bunny(matrix)

biggest_count, direction, eggs = find_biggest_path(matrix, bunny_coordinates)



print(direction)
for row in eggs:
    print(row)
print(biggest_count)