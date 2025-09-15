number_of_lines = int(input())
water_tank_capacity = 255
current_poored_water = 0
for line in range(number_of_lines):
    liters = int(input())
    current_poored_water += liters
    if current_poored_water > water_tank_capacity:
        print("Insufficient capacity!")
        current_poored_water -= liters
        continue
print(current_poored_water)



