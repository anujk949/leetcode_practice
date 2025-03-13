from data_structures.linkedList import LinkedList

class Queue:
    def __init__(self, max_length = None):
        self.queue = LinkedList()
        if isinstance(max_length, int) or max_length is None:
            self.max_length = max_length
        else:
            raise AttributeError("max_length should be integer type")

    def isEmpty(self):
        return self.queue.length == 0
    
    def isFull(self):
        if self.max_length:
            return self.queue.length == self.max_length
        return False
        
    def enqueue(self, value):
        if self.isFull():
            raise Exception ("Queue is already full")
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception ("No Element Found!")
        node = self.queue.popFirst()
        return node.data

    def peek(self):
        if self.isEmpty():
            raise Exception ("No Element Found!")
        node = self.queue.head
        return node.data
    
