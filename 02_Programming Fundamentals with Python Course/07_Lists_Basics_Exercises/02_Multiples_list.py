factor = int(input())
count = int(input())
my_list = []

for multiplier in range(1, count+1):
    current_number = factor * multiplier
    my_list.append(current_number)
print(my_list)
