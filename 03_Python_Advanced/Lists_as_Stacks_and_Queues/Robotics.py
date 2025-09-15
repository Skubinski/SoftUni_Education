from collections import deque

def convert_to_seconds(time):
    """Convert HH:MM:SS to total seconds."""
    hours, minutes, seconds = map(int, time.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_hms(seconds):
    """Convert total seconds to HH:MM:SS format."""
    seconds %= 86400
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

robots_details = input().split(';')
robots = {}
busy_until = {}

for bot in robots_details:
    name, process_time = bot.split('-')
    robots[name] = int(process_time)
    busy_until[name] = 0

current_time = convert_to_seconds(input())

products = deque()
command = input()
while command != "End":
    products.append(command)
    command = input()

# Process products
while products:
    current_time += 1

    for name in busy_until:
        if current_time >= busy_until[name]:
            product = products.popleft()
            busy_until[name] = current_time + robots[name]
            print(f"{name} - {product} [{seconds_to_hms(current_time)}]")
            break

    else:
        products.append(products.popleft())
