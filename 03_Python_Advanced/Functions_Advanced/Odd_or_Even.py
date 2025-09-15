import sys
from io import StringIO

test_input_1 = """Even
1 3 5 34 7 9 12 11 13 10
"""
sys.stdin = StringIO(test_input_1)

command = input()

numbers = [int (x) for x in input().split()]

if command == "Odd":
    print(sum([int (x) for x in numbers if x % 2 == 1]) * len(numbers))

else:
    print(sum([int(x) for x in numbers if x % 2 == 0]) * len(numbers))