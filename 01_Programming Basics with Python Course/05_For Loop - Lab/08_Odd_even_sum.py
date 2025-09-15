#input
n = int(input())
even = 0
odd = 0

for numbers in range(1,n + 1):
    current_number = int(input())
    if numbers % 2 == 0:
        even += current_number
    else:
        odd += current_number

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    difference = abs(even - odd)
    print("No")
    print(f"Diff = {difference}")