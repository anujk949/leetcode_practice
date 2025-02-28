class StackList:
    def __init__(self, max_length=None):
        self.stack = []
        self.length = 0
        self.max_length = max_length

    def size(self):
        return self.length
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(item)
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        self.length -= 1
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return self.length == 0


    def is_full(self):
        if self.max_length:
            return self.length == self.max_length
        else:
            False
    


class StackLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def size(self):
        pass


    def push(self, item):
        pass 
