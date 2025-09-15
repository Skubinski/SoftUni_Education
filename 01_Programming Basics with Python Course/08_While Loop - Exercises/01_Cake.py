#input
cake_length = int(input())
cake_width = int(input())
area = cake_width * cake_length
command = input()
while command != "STOP":
    current_number = int(command)
    area -= current_number
    if area <= 0:
        break
    command = input()
if area <= 0:
    print(f"No more cake left! You need {-area} pieces more.")
else:
    print(f"{area} pieces are left.")
