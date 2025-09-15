from math import floor
record_in_seconds = float(input())
distance = float(input())
time_in_seconds = float(input())
needed_time_in_seconds = distance * time_in_seconds
bonus_seconds = floor((distance / 50)) * 30
total_time = bonus_seconds + needed_time_in_seconds
if record_in_seconds <= total_time:
    print(f"No! He was {total_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")