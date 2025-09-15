rows, cols = [int(x) for x in input().split()]

matrix = []

# Read matrix
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    is_valid = True
    command = input()
    if command == "END":
        break

    command_arg = command.split()

    # Check if the command starts with "swap" and has exactly 5 elements
    if command_arg[0] == "swap":
        if len(command_arg) != 5:
            print("Invalid input!")
            continue

        # Check if all coordinates are valid (non-negative)
        for num in command_arg[1:]:
            if int(num) < 0:
                print("Invalid input!")
                is_valid = False
                break

        if not is_valid:
            continue

        # Convert the command arguments to integers for row and column indices
        row1, col1, row2, col2 = map(int, command_arg[1:])

        # Check if the coordinates are within the bounds of the matrix
        if row1 >= rows or row2 >= rows or col1 >= cols or col2 >= cols:
            print("Invalid input!")
            continue

        # Swap the elements in the matrix
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        # Print the updated matrix
        for row in matrix:
            print(*row)

    else:
        print("Invalid input!")
