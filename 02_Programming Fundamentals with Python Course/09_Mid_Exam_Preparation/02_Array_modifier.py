# Read the initial array values
initial_array = list(map(int, input().split()))

# Process commands until "end" is received
while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "swap":
        index1, index2 = map(int, command[1:])
        initial_array[index1], initial_array[index2] = initial_array[index2], initial_array[index1]
    elif command[0] == "multiply":
        index1, index2 = map(int, command[1:])
        initial_array[index1] *= initial_array[index2]
    elif command[0] == "decrease":
        initial_array = [x - 1 for x in initial_array]

# Print the modified array
print(", ".join(map(str, initial_array)))
