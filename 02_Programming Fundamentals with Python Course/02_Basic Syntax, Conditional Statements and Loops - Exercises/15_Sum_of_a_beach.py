
input_string = input()


input_string_lower = input_string.lower()


target_words = ["sand", "water", "fish", "sun"]
counter = 0

word_counts = {}


for word in target_words:
    count = input_string_lower.count(word)
    word_counts[word] = count
    counter += count



print(counter)
