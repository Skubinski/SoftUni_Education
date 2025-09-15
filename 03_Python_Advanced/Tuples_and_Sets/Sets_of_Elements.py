n, m = input().split()

set_one = set()
set_two = set()
for i in range(int(n)):
    number = int(input())
    set_one.add(number)

for j in range(int(m)):
    num = int(input())
    set_two.add(num)
intersection = set_one.intersection(set_two)

for el in intersection:
    print(el)