def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

def is_attacked(row, col, matrix):
    if matrix[row][col] == "K":
        return True
    return False
def is_knight(row, col, matrix):
    result = 0
    if is_inside(row - 2, col - 1, size) and is_attacked(row - 2, col - 1, matrix):
        result += 1

    if is_inside(row - 2, col  + 1, size) and is_attacked(row - 2, col + 1, matrix):
        result += 1

    if is_inside(row - 1, col - 2, size) and is_attacked(row - 1, col - 2, matrix):
        result += 1

    if is_inside(row - 1, col + 2, size) and is_attacked(row - 1, col + 2, matrix):
        result += 1

    if is_inside(row + 2, col - 1, size) and is_attacked(row + 2, col - 1, matrix):
        result += 1

    if is_inside(row + 2, col + 1, size) and is_attacked(row + 2, col + 1, matrix):
        result += 1

    if is_inside(row + 1, col - 2, size) and is_attacked(row + 1, col - 2, matrix):
        result += 1

    if is_inside(row + 1, col + 2, size) and is_attacked(row + 1, col + 2, matrix):
        result += 1

    return result


size = int(input())

matrix = []

for row in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    knights = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = is_knight(row,col,matrix)

            if counter:
                knights[(row, col)] = counter

    if len(knights) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0

    for coords, counter in knights.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1
print(removed_knights)