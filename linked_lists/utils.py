class LinkedListNode():

    def __init__(self, value):
        self.val = value
        self.nxt = None

    def __repr__(self):
        return '<LinkedListNode: {}>'.format(self.val)


class LinkedList():

    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for value in iterable:
                self.insert_node(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.nxt

    def __repr__(self):
        sll = self
        order = []
        for node in sll:
            order.append(node.val)
        return '<LinkedList: {}>'.format(order)

    def insert_node(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            node.nxt = current
            self.head = node
