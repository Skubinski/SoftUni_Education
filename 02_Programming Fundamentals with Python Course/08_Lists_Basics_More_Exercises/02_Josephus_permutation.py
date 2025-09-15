def josephus_permutation(lst, k):
    result = []
    index = 0

    while len(lst) > 0:
        index = (index + k - 1) % len(lst)
        result.append(lst.pop(index))

    return result

# Input: List and k value
input_list = list(map(int, input().split()))
k = int(input())

# Get the Josephus permutation and print the result without spaces
permutation = josephus_permutation(input_list, k)
print("[" + ",".join(map(str, permutation)) + "]")
