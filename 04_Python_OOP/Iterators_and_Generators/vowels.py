class Vowels:
    def __init__(self, word):
        self.word = word
        self.i = 0
        self.end = len(word) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current = self.word[self.i]
            self.i += 1
            if current in "AaEeIiUuOoYy":
                return current
        else:
            raise StopIteration()

s = Vowels("Abcdeifdf")
for char in s:
    print(char)


