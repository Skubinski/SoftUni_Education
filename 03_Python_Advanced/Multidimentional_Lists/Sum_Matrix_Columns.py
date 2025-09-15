import sys
from io import StringIO

test_input_1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""
#sys.stdin = StringIO(test_input_1)

def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix=[]
    for row_index in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

matrix = read_matrix()

n = len(matrix)

m = len(matrix[0])

column_sum = [0] * m
for i in range(n):
    row = matrix[i]
    for j in range(m):
        column_sum[j] += row[j]
for k in range(len(column_sum)):
    print(column_sum[k])