number_of_groups = int(input())

mussala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
for people in range(number_of_groups):
    climbers = int(input())
    if climbers <= 5:
        mussala_climbers += climbers
    elif 6 <= climbers <= 12:
        montblanc_climbers += climbers
    elif 13 <= climbers <= 25:
        kilimanjaro_climbers += climbers
    elif 26 <= climbers <= 40:
        k2_climbers += climbers
    elif climbers >= 41:
        everest_climbers += climbers
total_climbers = mussala_climbers + montblanc_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers
mussala_percents = mussala_climbers / total_climbers * 100
montblanc_percents = montblanc_climbers / total_climbers * 100
kilimanjaro_percents = kilimanjaro_climbers / total_climbers * 100
k2_percents = k2_climbers / total_climbers * 100
everest_percents = everest_climbers / total_climbers * 100

print(f"{mussala_percents:.2f}%")
print(f"{montblanc_percents:.2f}%")
print(f"{kilimanjaro_percents:.2f}%")
print(f"{k2_percents:.2f}%")
print(f"{everest_percents:.2f}%")
