def even(numbers):
    even_list = []
    for number in numbers:
        if int(number) % 2 == 0:
            even_list.append(int(number))
    return even_list
numbers = input().split()
print(even(numbers))