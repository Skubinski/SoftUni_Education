def groups():
    boundary = 0
    numbers = input().split(', ')
    while True:
        if len(numbers) <= 0:
            break
        boundary += 10
        boundary_nums = [int(num) for num in numbers if int(num) <= boundary]
        print(f"Group of {boundary}'s: {boundary_nums}")
        numbers = [num for num in numbers if int(num) not in boundary_nums]

groups()
