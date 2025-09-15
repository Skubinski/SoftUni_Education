matrix = input().split('|')
new_list = []
while matrix:
    new_list.append(matrix.pop().split())

for row in new_list:
    for j in row:
        print(j, end=' ')