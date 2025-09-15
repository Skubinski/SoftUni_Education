number = int(input())

names = set()
for _ in range(number):
    name = input()
    names.add(name)
for n in names:
    print(n)