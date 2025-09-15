seq_one = set(map(int, input().split()))
seq_two = set(map(int, input().split()))

num = int(input())

for _ in range(num):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            [seq_one.add(int(x)) for x in command[2:]]
        else:
            [seq_two.add(int(x)) for x in command[2:]]
    elif command[0] == "Remove":
        if command[1] == "First":
            seq_one = seq_one.difference([int(x) for x in command[2:]])
        else:
            seq_two = seq_two.difference([int(x) for x in command[2:]])
    elif command[0] == "Check":
        print(seq_one.issubset(seq_two) or seq_two.issubset(seq_one))

print(*sorted(seq_one), sep=", ")
print(*sorted(seq_two), sep=", ")