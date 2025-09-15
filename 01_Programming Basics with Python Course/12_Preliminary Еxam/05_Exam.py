group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
total_grade = 0
students_count = int(input())
for mark in range(students_count):
    grade = float(input())
    total_grade += grade
    if 2.00 <= grade <= 2.99:
        group_1 += 1
    elif 3.00 <= grade <= 3.99:
        group_2 += 1
    elif 4.00 <= grade <= 4.99:
        group_3 += 1
    elif grade >= 5.00:
        group_4 += 1
percent_1_group = group_1 / students_count * 100
percent_2_group = group_2 / students_count * 100
percent_3_group = group_3 / students_count * 100
percent_4_group = group_4 / students_count * 100

average = total_grade / students_count
print(f"Top students: {percent_4_group:.2f}%")
print(f"Between 4.00 and 4.99: {percent_3_group:.2f}%")
print(f"Between 3.00 and 3.99: {percent_2_group:.2f}%")
print(f"Fail: {percent_1_group:.2f}%")
print(f"Average: {average:.2f}")
