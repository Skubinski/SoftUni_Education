num = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(num):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

p1_percents = p1 / num * 100
p2_percents = p2 / num * 100
p3_percents = p3 / num * 100
p4_percents = p4 / num * 100
p5_percents = p5 / num * 100

print(f"{p1_percents:.2f}%")
print(f"{p2_percents:.2f}%")
print(f"{p3_percents:.2f}%")
print(f"{p4_percents:.2f}%")
print(f"{p5_percents:.2f}%")

