def make_bold(function):
    def wrapper(*name):
        result = function(*name)
        return f"<b>{result}</b>"
    return wrapper

def make_italic(function):
    def wrapper(*name):
        result = function(*name)
        return f"<i>{result}</i>"
    return wrapper

def make_underline(function):
    def wrapper(*name):
        result = function(*name)
        return f"<u>{result}</u>"
    return wrapper



@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"hello, {', '.join(args)}"
print(greet_all("asd","GGG"))