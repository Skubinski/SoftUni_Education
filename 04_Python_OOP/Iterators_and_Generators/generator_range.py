def genrange(start, end):
    while start <= end:
        yield start
        start += 1

print(list((x+1 for x in range(10))))

print(list(genrange(1, 10)))