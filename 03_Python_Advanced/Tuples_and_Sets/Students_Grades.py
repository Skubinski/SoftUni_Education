number = int(input())

students_grades = {}

for _ in range(number):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for student in students_grades.items():
    print(f"{student[0]} -> {' '. join([f"{el:.2f}" for el in student[1]])} (avg: {sum(student[1]) / len(student[1]):.2f})")