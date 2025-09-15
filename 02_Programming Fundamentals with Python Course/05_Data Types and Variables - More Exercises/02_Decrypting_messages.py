key = int(input())


number_of_lines = int(input())
message = ""
for number in range(number_of_lines):
    letter = input()
    letter_as_number = ord(letter)
    letter_as_number += key
    letter_as_string = chr(letter_as_number)
    message += letter_as_string

print(message)
