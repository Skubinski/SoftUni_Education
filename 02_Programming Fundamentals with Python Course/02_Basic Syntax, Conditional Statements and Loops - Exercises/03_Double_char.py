while True:
    input_string = input()

    if input_string == "End":
        break

    if input_string != "SoftUni":
        doubled_string = ""
        for char in input_string:
            doubled_string += char * 2
        print(doubled_string)
