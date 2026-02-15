class Queue:
    def __init__(self) -> None:
        self.items = []

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.size() == 0:
            return None
        last = self.peek()
        del self.items[-1]
        return last
