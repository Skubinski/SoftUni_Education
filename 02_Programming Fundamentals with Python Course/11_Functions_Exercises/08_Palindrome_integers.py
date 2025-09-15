def palindrome_numbers (numbers):
    for i in numbers:
        first_number = i[0]
        last_number = i[-1]
        if first_number == last_number:
            print("True")
        else:
            print("False")
number = input().split(", ")


palindrome_numbers(number)