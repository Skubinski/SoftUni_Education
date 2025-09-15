num = int(input())
cars = set()
for _ in range(num):
    command, number = input().split(', ')
    if command == "IN":
        cars.add(number)
    elif command == "OUT":
        cars.remove(number)

if cars:
    print('\n'.join(cars))
else:
    print("Parking Lot is Empty")