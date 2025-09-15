from collections import deque

kids = deque(input().split())

rotations = int(input())

while len(kids) > 1:
    kids.rotate(-rotations)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.pop()}")
        