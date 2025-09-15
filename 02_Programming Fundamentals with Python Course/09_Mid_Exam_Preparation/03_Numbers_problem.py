# Read input as a space-separated string and split it into a list of integers
numbers = list(map(int, input().split()))

# Calculate the average
average_number = sum(numbers) / len(numbers)

# Filter and collect numbers greater than the average
filtered_numbers = [num for num in numbers if num > average_number]

# Sort the filtered numbers in descending order
sorted_numbers = sorted(filtered_numbers, reverse=True)

# Print the top 5 numbers or "No" if there are none
if len(sorted_numbers) > 0:
    print(" ".join(map(str, sorted_numbers[:5])))
else:
    print("No")
