class Sequence_Repeat:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.i = 0
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations < self.num:
            if self.i >= len(self.seq):
                self.i = 0
            current = self.seq[self.i]
            self.i += 1
            self.iterations += 1
            return current
        else:
            raise StopIteration()

r = Sequence_Repeat('I Love Python', 3)
for i in r:
    print(i, end="")

