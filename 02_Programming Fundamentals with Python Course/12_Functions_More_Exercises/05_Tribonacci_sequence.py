def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 2]

    sequence = [1, 1, 2]

    for i in range(3, n):
        next_term = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_term)

    return sequence

# Input: Positive integer
n = int(input())

# Generate and print the Tribonacci sequence up to n terms
result = tribonacci(n)
print(" ".join(map(str, result)))
