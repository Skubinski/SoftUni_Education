n = int(input())

matrix = []
for row in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    command_args = input()
    if command_args == "END":
        break
    command, row, col, num = command_args.split()

    if int(row) > n or int(col) > n or int(row) < 0 or int(col) < 0:
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[int(row)][int(col)] += int(num)
    else:
        matrix[int(row)][int(col)] -= int(num)

for i in matrix:
    print(*i)