with open("numbers.txt") as file:
    sum = sum([int(row) for row in file.readlines()])
    print(sum)