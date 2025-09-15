input_as_str = input().split()
removed_numbers = int(input())
input_as_int = []
for number in range(len(input_as_str)):
    current_number = int(input_as_str[number])
    input_as_int.append(current_number)


for _ in range(removed_numbers):
    min_number = min(input_as_int)
    input_as_int.remove(min_number)

print(', '.join(map(str, input_as_int)))
