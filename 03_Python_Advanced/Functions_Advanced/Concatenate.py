def concatenate(*args):
    result = ""
    for i in args:
        result += i
    return result

print(concatenate("Soft", "Uni", "Is", "Great", "!"))