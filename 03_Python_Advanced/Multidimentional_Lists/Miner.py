def find_start(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "s":
                return row, col  # Return the starting coordinates

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size  # Check if the position is within bounds

def play_game():
    # Read the field size
    n = int(input())

    # Read the list of commands
    commands = input().split()

    # Read the matrix (field)
    matrix = [input().split() for _ in range(n)]

    # Find the starting position of the miner
    start_row, start_col = find_start(matrix)

    # Initializing the game variables
    miner_row, miner_col = start_row, start_col
    coal_count = sum(row.count('c') for row in matrix)  # Count total coal pieces
    collected_coal = 0

    # Process each command
    for command in commands:
        # Moving the miner based on the command
        if command == "up":
            new_row, new_col = miner_row - 1, miner_col
        elif command == "down":
            new_row, new_col = miner_row + 1, miner_col
        elif command == "left":
            new_row, new_col = miner_row, miner_col - 1
        elif command == "right":
            new_row, new_col = miner_row, miner_col + 1

        # Check if the new position is inside the field
        if is_inside(new_row, new_col, n):
            miner_row, miner_col = new_row, new_col

            # Check if the miner has reached coal
            if matrix[miner_row][miner_col] == "c":
                collected_coal += 1
                coal_count -= 1
                matrix[miner_row][miner_col] = "*"  # Replace coal with a star

            # Check if the miner has reached the end
            if matrix[miner_row][miner_col] == "e":
                print(f"Game over! ({miner_row}, {miner_col})")
                return

            # Check if the miner collected all the coal
            if coal_count == 0:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                return

    # If we finish all commands and haven't won or lost, print the remaining coal
    print(f"{coal_count} pieces of coal left. ({miner_row}, {miner_col})")

# Run the game
play_game()
