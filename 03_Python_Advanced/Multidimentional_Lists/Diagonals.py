n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = []

secondary_diagonal = []

for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])

for col_idx in range(n):
    secondary_diagonal.append(matrix[col_idx][n-1-col_idx])

print(f"Primary diagonal: {', '.join([str (x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str (x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

