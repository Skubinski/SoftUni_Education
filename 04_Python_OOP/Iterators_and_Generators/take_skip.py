class Take_Skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:
            current = self.i
            self.i += self.step
            self.generated += 1
            return current
        else:
            raise StopIteration()

nums = Take_Skip(10, 5)
for n in nums:
    print(n)