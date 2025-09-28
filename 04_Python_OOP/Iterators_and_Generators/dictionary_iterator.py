class Dictionary_Iter:
    def __init__(self, dict):
        self.dict = list(dict.items())
        self.i = 0
        self.end = len(dict) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            result = self.dict[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration()

r = Dictionary_Iter({1: "1", 2: "2"})
for x in r:
    print(x)


