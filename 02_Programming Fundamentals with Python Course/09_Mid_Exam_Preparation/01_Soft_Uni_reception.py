#input
employee_1_efficienty = int(input())
employee_2_efficienty = int(input())
employee_3_efficienty = int(input())

students_count = int(input())
#calculations

hours = 0

all_emloyes_efficienty_for_hour = employee_3_efficienty + employee_2_efficienty + employee_1_efficienty

while students_count > 0:
    students_count -= all_emloyes_efficienty_for_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

