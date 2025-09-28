def read_next(*args):
    for iterable in args:
        for el in iterable:
            yield el
for item in read_next("string", (2,), {"d":1, "I": 2}):
    print(item, end="")