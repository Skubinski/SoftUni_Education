def odd (text):
    odd_sum = 0
    for i in range(len(text)):
        current_number = int(text[i])
        if current_number % 2 != 0:
            odd_sum += current_number
    return odd_sum

def even (text):
    even_sum = 0
    for i in range(len(text)):
        current_number = int(text[i])
        if current_number % 2 == 0:
            even_sum += current_number
    return even_sum
text = input()
print(f"Odd sum = {odd(text)}, Even sum = {even(text)}")

