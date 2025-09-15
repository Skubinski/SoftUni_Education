def sort (list):
    list_as_int = []
    for i in list:
        list_as_int.append(int(i))
    sorted_list = sorted(list_as_int, reverse=False)
    return sorted_list
numbers = input().split()
print(sort(numbers))