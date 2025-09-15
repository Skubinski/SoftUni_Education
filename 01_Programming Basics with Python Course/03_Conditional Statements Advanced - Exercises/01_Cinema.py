type_projection = input()
number_rows = int(input())
number_columns = int(input())
cinema_capacity = number_columns * number_rows
income = 0
if type_projection == "Premiere":
    income = 12 * cinema_capacity
elif type_projection == "Normal":
    income = 7.50 * cinema_capacity
elif type_projection == "Discount":
    income = 5 * cinema_capacity
print(f'{income:.2f} leva')