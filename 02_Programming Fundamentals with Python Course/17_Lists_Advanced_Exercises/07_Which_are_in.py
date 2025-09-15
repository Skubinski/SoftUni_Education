sequence_one = input().split(", ")
sequence_two = input().split(", ")
list = []
for i in sequence_one:
    for j in sequence_two:
        if i in j:
            list.append(i)
            break
print(list)

