from math import ceil
#input
serial_name = input()
episode_duration = int(input())
break_duration = int(input())
#calculations
lunch_break_time = break_duration * (1 / 8)
breath_time = break_duration * (1 / 4)
rest_time = break_duration - (lunch_break_time + breath_time)
if rest_time >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {ceil(rest_time - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(episode_duration - rest_time)} more minutes.")