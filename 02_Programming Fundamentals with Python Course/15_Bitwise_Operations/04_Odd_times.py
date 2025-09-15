def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

list = input().split()
list_as_int = []
for i in list:
    list_as_int.append(int(i))


odd_occurrence = find_odd_occurrence(list_as_int)
print(odd_occurrence)


