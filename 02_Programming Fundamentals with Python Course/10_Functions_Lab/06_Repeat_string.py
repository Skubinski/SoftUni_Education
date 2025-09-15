def repeater (text, counter):
    new_text = text * counter
    return new_text
text = input()
counter = int(input())
print(repeater(text, counter))