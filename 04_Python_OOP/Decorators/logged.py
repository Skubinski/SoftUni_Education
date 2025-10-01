def logged(function):
    def wrapper(*numbers):
        func_name = function.__name__
        res = function(*numbers)
        result = f"you called {func_name}{numbers}\n"
        result += f"it returned {res}"
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4,4,4))