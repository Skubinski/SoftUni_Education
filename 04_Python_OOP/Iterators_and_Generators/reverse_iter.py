class ReverseIter:
    def __init__(self, obj):
        self.obj = obj
        self.i = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            current = self.obj[self.i]
            self.i -= 1
            return current
        else:
            raise StopIteration()

r = ReverseIter([1,2,3,4, 5, "a"])

for item in r:
    print(item)