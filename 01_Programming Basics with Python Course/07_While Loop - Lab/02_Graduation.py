#Input
total = 0
class_in_school = 1
bad_years = 0
name = input()

while class_in_school <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_years += 1
        if bad_years > 1:
            print(f"{name} has been excluded at {class_in_school} grade")
            break
        continue
    total += current_grade
    class_in_school +=1

else:
    average_grade = total / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")