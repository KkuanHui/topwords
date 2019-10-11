

class limitstack:
    def __init__(self, size, init_value):
        self.size = size
        self.stack = [init_value] * size
        self.head = size - 1
    def push(self, value):
        if head + 1 >= size: head = 0
        else: head += 1
        self.stack[head] = value
    def get(self, idx):
        if head - idx < 0: pos = self.size + self.head - idx
        else: pos = head - idx
        return self.stack[pos]
