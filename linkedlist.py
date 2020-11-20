class Node:
    def __init__(self, element=None, nextnode=None):
        self.element = element
        self.nextnode = nextnode

    def __str__(self):
        return f'{self.element} {self.nextnode}'


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addtohead(self, element):
        newnode = Node(element, self.head)
        self.head = newnode
        if self.tail is None:
            self.tail = newnode

    def addtoend(self, element):
        newnode = Node(element)
        if self.head is None or self.tail is None:
            self.head = newnode
            self.tail = newnode
        self.tail.nextnode = newnode
        self.tail = newnode

    def getNode(self, value):
        current = self.head
        count = 0
        while count <= value:
            if count == value:
                return current
            count += 1
            current = current.nextnode

    def remove(self, value):
        current = self.head
        next = current.nextnode
        count = 0
        while count < value:
            count += 1
            current = next
            next = current.nextnode
            if count == (value-1):
                next = next.nextnode
                current.nextnode = next
