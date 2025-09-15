from collections import deque
clients = deque()
command = input()
while not command == 'End':

    if command == 'Paid':
        while clients:
            client = clients.popleft()
            print(client)
    else:
        clients.append(command)


    command = input()
print(f"{len(clients)} people remaining.")