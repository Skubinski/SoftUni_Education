from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    if command == "green":
        current_green = green_light_duration

        while cars_queue and current_green > 0:
            car = cars_queue.popleft()
            car_length = len(car)

            if car_length <= current_green:
                current_green -= car_length
                total_cars_passed += 1
            else:
                car_length -= current_green
                if car_length <= free_window_duration:
                    total_cars_passed += 1
                else:
                    hit_char = car[current_green + free_window_duration]
                    print("A crash happened!")
                    print(f"{car} was hit at {hit_char}.")
                    exit()
        continue

    cars_queue.append(command)
