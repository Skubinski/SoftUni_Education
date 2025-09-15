def calculate_total_time(steps):
    total_time = sum(steps)
    if 0 in steps:
        total_time -= 0.2 * total_time
    return total_time

def announce_winner(left_steps, right_steps):
    left_total_time = calculate_total_time(left_steps)
    right_total_time = calculate_total_time(right_steps)

    if left_total_time < right_total_time:
        return f"The winner is left with total time: {left_total_time:.1f}"
    elif left_total_time > right_total_time:
        return f"The winner is right with total time: {right_total_time:.1f}"
    else:
        return "It's a tie!"

# Input sequence of numbers as a list of integers
sequence = list(map(int, input().split()))

# Calculate the middle index
middle_index = len(sequence) // 2

# Split the sequence into left and right parts
left_steps = sequence[:middle_index]
right_steps = sequence[middle_index + 1:]

# Announce the winner and print the result
print(announce_winner(left_steps, right_steps))
