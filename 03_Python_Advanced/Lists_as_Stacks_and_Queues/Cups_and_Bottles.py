from collections import deque

cups = deque(map(int, input().split()))  # queue (first entered cup - first filled)
bottles = list(map(int, input().split()))  # stack (last entered bottle - first used)

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    while current_cup > 0 and bottles:
        current_bottle = bottles.pop()
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
            current_cup = 0  # cup is filled
        else:
            current_cup -= current_bottle  # cup still needs more water

# Check what is left and print result
if not cups:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
