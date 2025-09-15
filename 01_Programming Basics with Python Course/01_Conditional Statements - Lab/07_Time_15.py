#input
hours = int(input())
minutes = int(input())
after_15 = minutes + 15
hours_after = 0
minutes_after = 0

if after_15 >= 60:
    minutes_after = after_15 % 15
    hours_after = hours + 1
else:
    minutes_after = after_15
    hours_after = hours

if hours_after == 24:
    hours_after = 0

if minutes_after < 10:
    print(f"{hours_after}:0{minutes_after}")
else:
    print(f"{hours_after}:{minutes_after}")