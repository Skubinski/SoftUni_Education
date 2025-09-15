#input
combination_number = 0
start = int(input())
final = int(input())
magic_number = int(input())
combination_is_found = False
for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        combination_number += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combination_number} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_number} combinations - neither equals {magic_number}")