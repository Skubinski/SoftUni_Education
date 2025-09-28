def squares(n):
    i = 1
    while i <= 5:
        yield i * i
        i += 1

print(list(squares(5)))