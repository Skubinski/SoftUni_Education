number_of_stages = int(input())
number_of_rooms_per_stage = int(input())
stage_letter = ""

for stages in range(number_of_stages, 0, -1):

    for rooms in range(number_of_rooms_per_stage):
        if stages == number_of_stages:
            stage_letter = "L"

        elif stages % 2 == 0:
            stage_letter = "O"

        else:
            stage_letter = "A"
        print(f"{stage_letter}{stages}{rooms}",end=" ")
    print()

