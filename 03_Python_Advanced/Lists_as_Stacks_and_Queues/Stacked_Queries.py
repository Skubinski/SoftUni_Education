def max_num(list):
    max_num = float('-inf')
    for num in list:
        if num > max_num:
            max_num = num
    return max_num

def min_num(list):
    min_num = float('inf')
    for num in list:
        if num < min_num:
            min_num = num
    return min_num

number_of_inputs = int(input())
stack = []
for num in range(number_of_inputs):
    command = input().split()

    if int(command[0]) == 1:
        stack.append(int(command[1]))

    elif int(command[0]) == 2:
        if stack:
            stack.pop()


    elif int(command[0]) == 3 and stack:
        print(max_num(stack))

    elif command[0] == '4' and stack:
        print(min_num(stack))

while stack:
    last_num = stack.pop()
    if not stack:
        print(last_num, end=' ')
    else:
         print(last_num, end=', ')