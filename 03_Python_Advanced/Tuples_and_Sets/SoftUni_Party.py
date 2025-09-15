guests = int(input())
vip = set()
regular = set()

for _ in range(guests):
    number = input()
    if number[0].isdigit():
        vip.add(number)
    else:
        regular.add(number)
command = input()

all = vip.union(regular)
while not command == "END":
    if command in all:
        if command[0].isdigit():
            vip.remove(command)
        else:
            regular.remove(command)
        all.remove(command)
    command = input()
print(len(all))
print('\n'.join(sorted(vip)))
print('\n'.join(sorted(regular)))