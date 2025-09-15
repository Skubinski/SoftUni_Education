def process_input(data_type, value):
    if data_type == "int":
        result = int(value) * 2
        return result
    elif data_type == "real":
        result = float(value) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        result = f"${value}$"
        return result
    else:
        return "Invalid data type"

text = input()
number = input()
print(process_input(text, number))
