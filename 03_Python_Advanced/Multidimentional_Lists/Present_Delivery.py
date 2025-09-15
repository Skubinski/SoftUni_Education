import sys
from io import StringIO

test_input_1 = """5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
"""
#sys.stdin = StringIO(test_input_1)

def find_santa(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "S":
                return (row, col)

def find_nice_kid(row, col, matrix):
    if matrix[row][col] == "V":
        return True
    return False
def find_cookie(row, col, matrix):
    if matrix[row][col] == "C":
        return True
    return False

def find_bad_kid(row, col, matrix):
    if matrix[row][col] == "X":
        return True
    return False

def find_neighbours(row, col, matrix):
    if matrix[row][col] != "-":
        return True
    return False

def nice_kids_counter(matrix):
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "V":
                counter += 1
    return counter

m = int(input())

n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())

santa_row, santa_col = find_santa(matrix)

given_presents = 0
while True:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"
    if command == "up":
        santa_row -= 1
        if find_nice_kid(santa_row, santa_col, matrix):
            m -= 1
            given_presents += 1
            matrix[santa_row][santa_col] = "S"
            if m <= 0:
                break
        if find_bad_kid(santa_row, santa_col, matrix):
            matrix[santa_row][santa_col] = "S"
        if find_cookie(santa_row, santa_col, matrix):
            matrix[santa_row][santa_col] = "S"
            if find_neighbours(santa_row - 1, santa_col, matrix):
                matrix[santa_row - 1][santa_col] = "-"
                m -= 1
                if m <= 0:
                    break
            if find_neighbours(santa_row + 1, santa_col, matrix):
                matrix[santa_row + 1][santa_col] = "-"
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                m -= 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col + 1, matrix):
                matrix[santa_row][santa_col + 1] = "-"
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                m -= 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col - 1, matrix):
                matrix[santa_row][santa_col - 1] = "-"
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                m -= 1
                if m <= 0:
                    break


    elif command == "down":
        santa_row += 1
        if find_nice_kid(santa_row, santa_col, matrix):
            m -= 1
            given_presents += 1
            matrix[santa_row][santa_col] = "S"
            if m <= 0:
                break
        if find_bad_kid(santa_row, santa_col, matrix):
            matrix[santa_row][santa_col] = "S"
        if find_cookie(santa_row, santa_col, matrix):
            if find_neighbours(santa_row - 1, santa_col, matrix):
                matrix[santa_row - 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row + 1, santa_col, matrix):
                matrix[santa_row + 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col + 1, matrix):
                matrix[santa_row][santa_col + 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row - 1, santa_col - 1, matrix):
                matrix[santa_row][santa_col - 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
    elif command == "right":
        santa_col += 1
        if find_nice_kid(santa_row, santa_col, matrix):
            m -= 1
            matrix[santa_row][santa_col] = "S"
            given_presents += 1
            if m <= 0:
                break
        if find_bad_kid(santa_row, santa_col, matrix):
            matrix[santa_row][santa_col] = "S"
        if find_cookie(santa_row, santa_col, matrix):
            if find_neighbours(santa_row - 1, santa_col, matrix):
                matrix[santa_row - 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row + 1, santa_col, matrix):
                matrix[santa_row + 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col + 1, matrix):
                matrix[santa_row][santa_col + 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row - 1, santa_col - 1, matrix):
                matrix[santa_row][santa_col - 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
    elif command == "left":
        santa_col -= 1
        if find_nice_kid(santa_row, santa_col, matrix):
            m -= 1
            matrix[santa_row][santa_col] = "S"
            given_presents += 1
            if m <= 0:
                break
        if find_bad_kid(santa_row, santa_col, matrix):
            matrix[santa_row][santa_col] = "S"
        if find_cookie(santa_row, santa_col, matrix):
            if find_neighbours(santa_row - 1, santa_col, matrix):
                matrix[santa_row - 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row + 1, santa_col, matrix):
                matrix[santa_row + 1][santa_col] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col + 1, matrix):
                matrix[santa_row][santa_col + 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
            if find_neighbours(santa_row, santa_col - 1, matrix):
                matrix[santa_row][santa_col - 1] = "-"
                m -= 1
                if find_nice_kid(santa_row,santa_col,matrix):
                    given_presents += 1
                if m <= 0:
                    break
counter = nice_kids_counter(matrix)
if m <= 0 and counter > 0:
    print("Santa ran out of presents!")
else:
    print()

for row in matrix:
    print(*row)

if counter > 0:
    print(f"No presents for {counter} nice kid/s.")
else:
    print(f"Good job, Santa! {given_presents} happy nice kid/s.")