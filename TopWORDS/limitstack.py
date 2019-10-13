

"""
stack
size = 6
[0 1 2 3 4 5]
"""

class limitstack:
    def __init__(self, size, init_value):
        self.size = size
        self.stack = [init_value] * size
        self.head = size - 1
    def push(self, value):
        if self.head + 1 >= self.size: self.head = 0
        else: self.head += 1
        self.stack[self.head] = value
    def get(self, idx):
        if self.head - idx < 0: pos = self.size + self.head - idx
        else: pos = self.head - idx
        return self.stack[pos]
