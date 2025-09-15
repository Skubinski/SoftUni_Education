# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
space_width = int(input())
space_length = int(input())
space_heigth = int(input())
space_area = space_heigth * space_width * space_length
command = input()
while command != "Done":
    current_number = int(command)
    space_area -= current_number
    if space_area <= 0:
        break
    command = input()
if space_area <= 0:
    print(f"No more free space! You need {-space_area} Cubic meters more.")
else:
    print(f"{space_area} Cubic meters left.")
