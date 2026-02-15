class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
