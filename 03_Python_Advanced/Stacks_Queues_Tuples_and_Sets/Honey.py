from collections import deque
working_bees = deque(input().split())

nectar = input().split()

symbols = deque(input().split())
total_honey = 0
while True:
    if len(nectar) == 0 or len(working_bees) == 0:
        break
    honey = 0
    first_bee = int(working_bees.popleft())

    last_nectar = int(nectar.pop())

    first_symbol = symbols.popleft()
    if last_nectar >= first_bee:
        if first_symbol == "+":
            honey = first_bee + last_nectar
            total_honey += abs(honey)
        elif first_symbol == "-":
            honey = first_bee - last_nectar
            total_honey += abs(honey)
        elif first_symbol == "*":
            honey = first_bee * last_nectar
            total_honey += abs(honey)
        else:
            if last_nectar == 0:
                continue
            honey = first_bee / last_nectar
            total_honey += abs(honey)

    else:
        working_bees.appendleft(str(first_bee))
        symbols.appendleft(first_symbol)
        continue

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {", ".join(working_bees)}")
else:
    print(f"Nectar left: {", ".join(nectar)}")