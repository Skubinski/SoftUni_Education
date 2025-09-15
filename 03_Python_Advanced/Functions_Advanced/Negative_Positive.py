import sys
from io import StringIO

test_input_1 = """1 2 -3 -4 65 -98 12 57 -84
"""
sys.stdin = StringIO(test_input_1)


numbers = [int(x) for x in input().split()]

positive_numbers = [int (x) for x in numbers if x > 0]
negative_numbers = [int (x) for x in numbers if x < 0]

print(sum(negative_numbers))
print(sum(positive_numbers))

if abs(sum(negative_numbers)) > abs(sum(positive_numbers)):
    print("The negatives are stronger than the positives")

else:
    print("The positives are stronger than the negatives")
