numbers = (float (x) for x in input().split())
count = {}

for num in numbers:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1
for digit, counts in count.items():
    print(f"{digit} - {counts} times")