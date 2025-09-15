num = int(input())

elements = set()

for _ in range(num):
    el = input().split()
    for j in el:
        elements.add(j)

for i in elements:
    print(i)