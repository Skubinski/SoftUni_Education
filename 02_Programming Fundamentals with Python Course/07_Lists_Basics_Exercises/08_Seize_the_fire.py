input_line = input()
fire_cells = input_line.split("#")
effort = 0
fire = 0
water = int(input())
cells = []

for cell in fire_cells:
    fire_type, cell_value = cell.split(" = ")
    cell_value = int(cell_value)

    if fire_type == "High" and 81 <= cell_value <= 125:
        if water >= cell_value:
            water -= cell_value
            fire += cell_value
            cells.append(cell_value)
            effort += 0.25 * cell_value
    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        if water >= cell_value:
            water -= cell_value
            fire += cell_value
            cells.append(cell_value)
            effort += 0.25 * cell_value
    elif fire_type == "Low" and 1 <= cell_value <= 50:
        if water >= cell_value:
            water -= cell_value
            fire += cell_value
            cells.append(cell_value)
            effort += 0.25 * cell_value

print("Cells:")
for el in cells:
    print(f" - {el:.0f}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
