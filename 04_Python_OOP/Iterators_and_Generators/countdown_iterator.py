class Countdown_Iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            current = self.count
            self.count -= 1
            return current
        else:
            raise StopIteration()

it = Countdown_Iterator(10)
for i in it:
    print(i, end=" ")