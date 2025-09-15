def get_neighbors(row, col, size):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < size and 0 <= c < size:
            neighbors.append((r, c))
    return neighbors

# Input handling
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs_input = input().split()
bombs = [tuple(map(int, bomb.split(','))) for bomb in bombs_input]

for row, col in bombs:
    if matrix[row][col] > 0:  # if the bomb is still alive
        bomb_value = matrix[row][col]
        for r, c in get_neighbors(row, col, n):
            if matrix[r][c] > 0:
                matrix[r][c] -= bomb_value
        matrix[row][col] = 0

# Calculate alive cells
alive_cells = [cell for row in matrix for cell in row if cell > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

# Print matrix
for row in matrix:
    print(' '.join(str(cell) for cell in row))
