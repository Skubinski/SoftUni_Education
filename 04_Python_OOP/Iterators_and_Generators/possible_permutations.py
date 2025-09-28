from itertools import permutations
def possible_permutations(obj):
    result = permutations(obj)

    for perm in result:
        yield list(perm)
a = [print(p) for p in possible_permutations([1,2,3])]

