text = input()

count = {}

for letter in text:
    if letter not in count:
        count[letter] = 1
    else:
        count[letter] += 1

for x in sorted(count.items()):
    print(f"{x[0]}: {x[1]} time/s")