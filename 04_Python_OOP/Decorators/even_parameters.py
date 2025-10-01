def even_parameters(function):
    def wrapper(*args):
        for el in args:
            if not is_even(el):
                return "Please use only even numbers!"
        result = function(*args)
        return result

    return wrapper

def is_even(num):
    if isinstance(num, int) and num % 2 == 0:
        return True
    return False




@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(2,4,6,8))
print(multiply(2,4,9,8))