clothes = [int(x) for x in input().split()]

capacity = int(input())


rack_count = 1

current_rack_usage = 0
while clothes:

    last_cloth = clothes.pop()
    current_rack_usage += last_cloth

    if current_rack_usage > capacity:
        rack_count += 1
        current_rack_usage = last_cloth

print(rack_count)