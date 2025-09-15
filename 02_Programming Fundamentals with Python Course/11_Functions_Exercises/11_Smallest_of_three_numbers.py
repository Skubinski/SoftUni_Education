def smallest (a, b, c):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    return min(list)
a = int(input())
b = int(input())
c = int(input())
print(smallest(a, b, c))