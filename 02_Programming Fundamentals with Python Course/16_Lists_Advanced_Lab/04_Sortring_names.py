def sorted_names (given_names):
    sorted_given_names = sorted(given_names, key=lambda x: (-len(x), x))
    return sorted_given_names


names = input().split(', ')
print(sorted_names(names))