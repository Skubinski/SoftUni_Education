first_multiplicator = 1
while first_multiplicator <= 10:
    second_multiplicator = 1
    while second_multiplicator <= 10:
        print(f"{first_multiplicator} * {second_multiplicator} = {first_multiplicator * second_multiplicator}")
        second_multiplicator +=1
    first_multiplicator += 1
#
# for first_multiplicator in range(1,11):
#     for second_multiplicator in range(1, 11):
#         print(f"{first_multiplicator} * {second_multiplicator} = {first_multiplicator * second_multiplicator}")