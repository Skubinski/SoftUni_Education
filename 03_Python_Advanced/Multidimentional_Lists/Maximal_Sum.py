rows, cols = [int(x) for x in input().split()]


matrix = []

max_sum = 0

biggest_3_x_3 = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):

    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + \
                      matrix[row][col + 2] + matrix[row + 1][col] + \
                      matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_3_x_3 = [
                matrix[row][col:col + 3],
                matrix[row + 1][col:col + 3],
                matrix[row + 2][col:col + 3]
            ]

print(f"Sum = {max_sum}")
for row in biggest_3_x_3:
    print(*row, sep=' ')

