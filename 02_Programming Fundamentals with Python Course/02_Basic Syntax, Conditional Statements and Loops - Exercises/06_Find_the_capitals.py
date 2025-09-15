
input_string = input()

capital_indices = []


for index, char in enumerate(input_string):

    if char.isupper():
        capital_indices.append(index)


print(capital_indices)
