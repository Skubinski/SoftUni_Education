from collections import deque

def max_num(list):
    max_num = float('-inf')
    for num in list:
        if num > max_num:
            max_num = num
    return max_num

total_food = int(input())

clients = deque([int(x) for x in input().split()])
print(max_num(clients))

while clients:
    if total_food - clients[0] >= 0:
        total_food -= clients.popleft()
    else:
        print("Orders left: " + " ".join([str(x) for x in clients]))
        break
if not clients:
    print("Orders complete")