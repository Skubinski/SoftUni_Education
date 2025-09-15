def exchange_command(nums, index):
    if 0 <= index < len(nums):
        left_sublist = nums[:index + 1]
        right_sublist = nums[index + 1:]
        return right_sublist + left_sublist
    else:
        return "Invalid index"

def max_min_command(nums, command):
    is_even = "even" in command
    max_min_value = float('-inf') if is_even else float('inf')
    max_min_index = -1

    for i in range(len(nums)):
        if (is_even and nums[i] % 2 == 0) or (not is_even and nums[i] % 2 != 0):
            if (is_even and nums[i] >= max_min_value) or (not is_even and nums[i] <= max_min_value):
                max_min_value = nums[i]
                max_min_index = i

    if max_min_index == -1:
        return "No matches"
    else:
        return max_min_index

def first_last_command(nums, command, count):
    is_first = "first" in command
    is_even = "even" in command
    result = []

    for num in nums:
        if (is_even and num % 2 == 0) or (not is_even and num % 2 != 0):
            result.append(num)
            if len(result) == count:
                break

    if is_first:
        return result[:count]
    else:
        return result[-count:]

# Input: Initial list
initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]

    if action == "end":
        break

    if action == "exchange":
        index = int(command[1])
        initial_list = exchange_command(initial_list, index)
    elif action in ["max", "min"]:
        result = max_min_command(initial_list, command[1])
        if result != "No matches":
            print(result)
        else:
            print(result)
    elif action in ["first", "last"]:
        count = int(command[1])
        sub_list = first_last_command(initial_list, command[2], count)
        if not sub_list:
            print("[]")
        else:
            print(sub_list)

# Print the final state of the list
print(f"[{', '.join(map(str, initial_list))}]")
