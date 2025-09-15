def is_valid_password(password):
    is_length = False
    is_only_char_and_digits = False
    is_at_least_two_digits = False
    digits_counter = 0
    if 6 <= len(password) <= 10:
        is_length = True
    if password.isalnum():
        is_only_char_and_digits = True
    for char in password:
        if char.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        is_at_least_two_digits = True
    if is_length and is_at_least_two_digits and is_only_char_and_digits:
        print("Password is valid")
    if is_length == False:
        print("Password must be between 6 and 10 characters")
    if is_only_char_and_digits == False:
        print("Password must consist only of letters and digits")
    if is_at_least_two_digits == False:
        print("Password must have at least 2 digits")


password = input()
is_valid_password(password)