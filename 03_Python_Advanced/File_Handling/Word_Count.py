import re

searched_words = []

with open("words.txt") as words:
    searched_words = words.read().split()

words_count = {}
with open("input.txt") as input:
    text = input.read()
    for word in searched_words:
        pattern = fr"\b{word}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))
        words_count[word] = count

sorted_dict = sorted(words_count.items(), key=lambda kvpt: -kvpt[1])


with open ("output.txt", "a") as output:
    for key, value in sorted_dict:
        output.write(f"{key} - {value}\n")