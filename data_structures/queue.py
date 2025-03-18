from data_structures.linkedList import LinkedList

class Queue:
    """
    Linked List implementation
    """
    def __init__(self, max_length:int = None):
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
    


class QueueUsingList:
    """
    Implement Queue using python list
    1. Circular Queue
    2. Priority Queue - ASC, DESC
    """

    def __init__(self, max_length: int = None):
        self.max_length = max_length
        self.length = 0
        self.right = self.left = 0
        if self.max_length:
            self.__queue = [-1]*max_length
        else:
            self.__queue = []


    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        if self.max_length:
            return self.length == self.max_length
        else:
            return False

    def enqueue(self, val):
        if self.isFull():
            raise Exception("Queue is already full")
        self.__queue[self.right] = val
        self.length+=1
        self.right+=1
        if self.max_length:
            self.right = self.right % self.max_length
        print("right",self.right)

    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        popped_item = self.__queue[self.left]
        self.length -= 1
        self.left +=1
        if self.max_length:
            self.left = self.left % self.max_length
        return popped_item
    
    @property
    def queue(self):
        if self.max_length:
            temp = []
            curr = self.left
            for i in range(self.length):
                print(curr)
                temp.append(self.__queue[curr])
                curr += 1
                curr = curr % self.max_length

            return temp
        return self.__queue[self.left:self.right]