import sys
from io import StringIO

test_input_1 = """2
1, 2, 3
4, 5, 6
"""
#sys.stdin = StringIO(test_input_1)
def read_matrix():
    n = int(input())
    matrix = []
    for row_index in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix

matrix = read_matrix()

print([i for row in matrix for i in row])