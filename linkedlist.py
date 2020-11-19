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