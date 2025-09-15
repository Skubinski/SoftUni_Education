def sum_set(set):
    sum = 0
    for num in set:
        sum+=num
    return sum

number = int(input())
odd = set()
even = set()
for row in range(number):
    name = input()
    sum = 0
    for char in name:
        sum += ord(char)
    sum /= row + 1
    if int(sum) % 2 == 0:
        even.add(int(sum))
    else:
        odd.add(int(sum))

odd_sum = sum_set(odd)
even_sum = sum_set(even)

if odd_sum == even_sum:
    print(', '.join(str(x) for x in odd.union(even)))
elif odd_sum > even_sum:
    print(', '.join(str(x) for x in odd.difference(even)))
else:
    print(', '.join(str(x) for x in odd.symmetric_difference(even)))