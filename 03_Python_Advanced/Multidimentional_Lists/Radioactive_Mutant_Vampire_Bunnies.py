def find_player(matrix, n, m):
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == "P":
                return row, col

def in_lair(p_row, p_col, n, m):
    return 0 <= p_row < n and 0 <= p_col < m

def spread_bunnies(matrix, n, m):
    new_bunnies = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 'B':
                # Spread the bunny to all 4 directions if in bounds
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == '.':
                        new_bunnies.append((nr, nc))
    # Add the new bunnies to the matrix
    for r, c in new_bunnies:
        matrix[r][c] = 'B'

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def game():
    # Read the dimensions of the lair
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]  # Create the matrix from input
    commands = input().strip()  # Read the commands

    # Find initial player position
    player_row, player_col = find_player(matrix, n, m)
    is_dead = False
    is_out = False

    # Process the commands
    for command in commands:
        # Spread the bunnies before the player moves
        spread_bunnies(matrix, n, m)

        # Move the player based on the command
        if command == "U":
            if in_lair(player_row - 1, player_col, n, m):
                player_row -= 1
        elif command == "D":
            if in_lair(player_row + 1, player_col, n, m):
                player_row += 1
        elif command == "L":
            if in_lair(player_row, player_col - 1, n, m):
                player_col -= 1
        elif command == "R":
            if in_lair(player_row, player_col + 1, n, m):
                player_col += 1

        # Check if the player is on a bunny or out of bounds
        if matrix[player_row][player_col] == "B":
            is_dead = True
            break
        if not in_lair(player_row, player_col, n, m):
            is_out = True
            break

        # Update the player's position on the matrix
        matrix[player_row][player_col] = "P"

    # Final output
    print_matrix(matrix)
    if is_out:
        print(f"won: {player_row} {player_col}")
    elif is_dead:
        print(f"dead: {player_row} {player_col}")

# Run the game
game()
