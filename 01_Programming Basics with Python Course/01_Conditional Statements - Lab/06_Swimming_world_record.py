from math import ceil, floor
#input
record_in_seconds = float(input())
distance_in_metres = float(input())
one_metre_time = float(input())
#calculations
needed_seconds =  distance_in_metres * one_metre_time

water_resistance = floor(distance_in_metres / 15) * 12.5

total_time = needed_seconds + water_resistance

#conditions
if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_difference = total_time - record_in_seconds
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")