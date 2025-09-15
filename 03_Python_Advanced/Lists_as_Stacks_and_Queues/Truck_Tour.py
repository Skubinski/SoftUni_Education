from collections import deque

stations = deque()
petrol_pumps_number = int(input().strip())
tank = 0
start_index = 0
total_fuel = 0
curr_fuel = 0

for i in range(petrol_pumps_number):
    amount, distance = map(int, input().split())
    stations.append((amount, distance))
    total_fuel += amount - distance  # Track total fuel balance

# If total fuel is negative, no solution exists (but it's guaranteed there is one)
if total_fuel < 0:
    print(-1)
else:
    for i in range(petrol_pumps_number):
        amount, distance = stations[i]
        curr_fuel += amount - distance

        if curr_fuel < 0:
            start_index = i + 1  # Reset start point
            curr_fuel = 0  # Reset the tank for a new attempt

    print(start_index)
