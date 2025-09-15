import sys
from io import StringIO

test_input_1 = """3
11 2 4
4 5 6
10 8 -12
"""
#sys.stdin = StringIO(test_input_1)

def read_matrix():
    n = int(input())
    matrix=[]
    for row_index in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

matrix = read_matrix()

n = len(matrix)

m = len(matrix[0])
diagonal_sum = 0
for i in range(n):
    for j in range(m):
        if i == j:
            diagonal_sum += matrix[i][j]
print(diagonal_sum)
