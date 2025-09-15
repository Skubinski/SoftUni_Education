number_of_lines = int(input())
word = input()
list = []
filtered_list = []

for line in range(number_of_lines):
    some_strings = input()
    list.append(some_strings)
    if word in some_strings:
        filtered_list.append(some_strings)
print(list)
print(filtered_list)
