def change(string):
    list_with_words = []

    for num in string:
        digits_as_chars = []
        other_chars = []
        for j in range(len(num)):
            current_text = num
            current_sign = num[j]
            if current_sign.isdigit():
                digits_as_chars.append(current_sign)
            else:
                other_chars.append(current_sign)
                continue

        total_digit = ''.join(digits_as_chars)
        other_chars_formated = ''.join(other_chars)
        num_as_chars = chr(int(total_digit))
        printed_text = num_as_chars + other_chars_formated



        list_with_words .append(printed_text)
    return list_with_words

text = input().split()
correct_list = []
for m in change(text):
    if len(m) <= 2:
        correct_list.append(m)
        continue
    else:

        first_letter = m[0]
        middle_letter = m[2:-1]
        second_letter = m[-1]
        last_letter = m[1]
        final_sentence = first_letter + second_letter + middle_letter + last_letter

        correct_list.append(final_sentence)
print(' '.join(correct_list))







