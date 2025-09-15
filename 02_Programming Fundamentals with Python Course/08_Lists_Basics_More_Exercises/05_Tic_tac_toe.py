def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 1:
            return "First player won"
        if board[i][0] == board[i][1] == board[i][2] == 2:
            return "Second player won"
        if board[0][i] == board[1][i] == board[2][i] == 1:
            return "First player won"
        if board[0][i] == board[1][i] == board[2][i] == 2:
            return "Second player won"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 1:
        return "First player won"
    if board[0][0] == board[1][1] == board[2][2] == 2:
        return "Second player won"
    if board[0][2] == board[1][1] == board[2][0] == 1:
        return "First player won"
    if board[0][2] == board[1][1] == board[2][0] == 2:
        return "Second player won"

    # If no winner, it's a draw
    return "Draw!"

# Input
board = []
for _ in range(3):
    row = list(map(int, input().split()))
    board.append(row)

# Check and print the result
result = check_winner(board)
print(result)
