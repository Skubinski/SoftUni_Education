import time
def exec_time(func):
    def wrapper(start, end):
        st = time.time()
        result = func(start, end)
        end = time.time()
        return end-st
    return wrapper

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x


print(loop(1, 10000000))