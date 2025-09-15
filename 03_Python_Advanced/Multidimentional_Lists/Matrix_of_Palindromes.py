rows, cols = [int(x) for x in input().split()]

starting = 97

for row in range(rows):
    middle = starting
    for col in range(cols):
        print(f"{chr(starting)}{chr(middle)}{chr(starting)}", end=' ')
        middle += 1
    starting += 1
    print()