def up(n):
    for row in range(1, n + 1):
        for space in range(n - row):
            print(" ", end='')
        for star in range(1, row):
            print('*', end=" ")

        print('*')

def down(n):
    for row in range(n - 1, 0, -1):
        for space in range(n - row):
            print(" ", end='')
        for star in range(1, row):
            print('*', end=" ")

        print("*")

def rhombus(n):
    up(n)
    down(n)

n = int(input())
rhombus(n)


