class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        #     temp = None
        #     for n in self:
        #         temp = n
        #     temp.next = node

    def add_to_head(self, node):
        if self.head is None:
            self.tail = node
        node.next = self.head
        self.head = node

    def remove_from_head(self):
        if self.head is None:
            return None
        head = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        head.next = None
        return head
