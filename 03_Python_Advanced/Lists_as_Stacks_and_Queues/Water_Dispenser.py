from collections import deque

quantity = int(input())

command = input()
queue = deque()
while not command == 'Start':
    queue.append(command)
    command = input()

command = input()
while not command == 'End':
    if command.isdigit():
        required_litters = int(command)
        if required_litters <= quantity:
            quantity -= required_litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    else:
        _, reffiled = command.split(' ')
        reffiled_litters = int(reffiled)
        quantity += reffiled_litters

    command = input()

print(f"{quantity} liters left")



