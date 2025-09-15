happiness = input().split()
factor = int(input())
new_happiness = [int(num) * factor for num in happiness]
average_happiness = sum(new_happiness) / len(new_happiness)
happy_employees = [employee for employee in new_happiness if employee >= average_happiness]
happy_counter = len(happy_employees)
if happy_counter >= len(new_happiness) / 2:
    print(f"Score: {happy_counter}/{len(new_happiness)}. Employees are happy!")
else:

    print(f"Score: {happy_counter}/{len(new_happiness)}. Employees are not happy!")
