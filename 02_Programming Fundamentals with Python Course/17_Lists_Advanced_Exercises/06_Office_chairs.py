rooms = int(input())
are_needed = False
chairs_sum_total = 0
people_sum_total = 0
for room in range(1, rooms + 1):
    chairs_sum = 0
    people_sum = 0
    count = input().split()
    people_sum += int(count[1])
    people_sum_total += int(count[1])
    chairs_sum += len(count[0])
    chairs_sum_total += len(count[0])
    if people_sum > chairs_sum:
        print(f"{people_sum - chairs_sum} more chairs needed in room {room}")
        are_needed = True
if are_needed == False:
    print(f"Game On, {chairs_sum_total - people_sum_total} free chairs left")


