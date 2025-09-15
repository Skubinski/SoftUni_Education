# Receive the initial gifts as a list
gifts = input().split()

# Process commands until "No Money" is received
while True:
    command = input().split()

    if command[0] == "No":
        break

    if command[0] == "OutOfStock":
        gift_to_remove = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif command[0] == "Required":
        gift_to_replace = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

# Filter out "None" gifts and print the result
filtered_gifts = [gift for gift in gifts if gift != "None"]
print(' '.join(filtered_gifts))
