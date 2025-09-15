# Input: Read an integer year
year = int(input())

# Find the next happy year
while True:
    year += 1
    year_str = str(year)
    if len(year_str) == len(set(year_str)):
        break

print(year)
