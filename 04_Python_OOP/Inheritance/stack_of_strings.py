class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        return f"{self.data[::-1]}"

s = Stack()
s.push("a")
s.push("b")
s.push("c")
s.push("d")
print(s.pop())
print(s.top())
print(s.is_empty())
print(s)