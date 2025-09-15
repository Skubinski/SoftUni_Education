#Input
from math import ceil, floor
processors_count = int(input())
employers_count = int(input())
working_days = int(input())
#calculations
total_hours = employers_count * working_days * 8
processors = floor(total_hours / 3)
if processors < processors_count:
    processors_needed = processors_count - processors
    losses = processors_needed * 110.10
    print(f"Losses: -> {losses:.2f} BGN")
else:
    more_processors = processors - processors_count
    profit = more_processors * 110.10
    print(f"Profit: -> {profit:.2f} BGN")
