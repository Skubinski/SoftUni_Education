n = int(input())

current_num = 1
row = 1

while current_num <= n:
    for _ in range(row):
        if current_num > n:
            break
        print(current_num, end=" ")
        current_num += 1
    print()
    row += 1
