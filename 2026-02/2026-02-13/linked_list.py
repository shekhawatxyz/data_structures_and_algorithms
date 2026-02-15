class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return self.val


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
        else:
            ref = None
            for n in self:
                ref = n
            ref.next = node
