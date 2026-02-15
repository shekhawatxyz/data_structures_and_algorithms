class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

    def set_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return self.value


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
            # ref = self.tail
            # for n in self:
            #     ref = n
            # ref.next = node
            self.tail.next = node
            self.tail = node

    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.next = None
        return temp

    # def add_to_head(self,node):
    #     if self.head == None:
    #         self.head = node
    #         self.tail = node
    #     else:
    #         node.next = self.head
    #         self.head = node
