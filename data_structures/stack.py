from data_structures.linkedList import LinkedList

class StackList:
    def __init__(self, max_length=None):
        """
        Initialize the stack with an optional maximum length.
        
        Args:
            max_length (int, optional): The maximum number of elements the stack can hold. Defaults to None.
        """
        self.stack = []
        self.length = 0
        self.max_length = max_length

    def size(self):
        """
        Get the current size of the stack.
        
        Returns:
            int: The number of elements in the stack.
        """
        return self.length
    
    def push(self, item):
        """
        Push an item onto the stack.
        
        Args:
            item: The item to be pushed onto the stack.
        
        Raises:
            Exception: If the stack is full.
        """
        if self.isFull():
            raise Exception("Stack is full")
        self.stack.append(item)
        self.length += 1

    def pop(self):
        """
        Pop the top item off the stack.
        
        Returns:
            The top item of the stack if the stack is not empty, otherwise None.
        """
        if self.isEmpty():
            return None
        self.length -= 1
        return self.stack.pop()
    
    def peek(self):
        """
        Peek at the top item of the stack without removing it.
        
        Returns:
            The top item of the stack if the stack is not empty, otherwise None.
        """
        if self.isEmpty():
            return None
        return self.stack[-1]
    
    def isEmpty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, otherwise False.
        """
        return self.length == 0

    def isFull(self):
        """
        Check if the stack is full.
        
        Returns:
            bool: True if the stack is full, otherwise False.
        """
        if self.max_length:
            return self.length == self.max_length
        else:
            return False

    def __len__(self):
        return self.size()


class StackUsingLinkedList:
    def __init__(self, max_length: int = None):
        """
        Initialize the stack with an optional maximum length.

        Args:
            max_length (int, optional): The maximum number of elements the stack can hold. Defaults to None.
        """
        self.stack = LinkedList()
        self.max_length = max_length

    def size(self):
        """
        Get the current size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)
    
    def __len__(self):
        """
        Get the current size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return self.size()

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, otherwise False.
        """
        return len(self.stack) == 0
    
    def isFull(self):
        """
        Check if the stack is full.

        Returns:
            bool: True if the stack is full, otherwise False.
        """
        if self.max_length:
            return len(self.stack) == self.max_length
        else:
            return False
        
    def push(self, val):
        """
        Push an item onto the stack.

        Args:
            val: The item to be pushed onto the stack.

        Raises:
            Exception: If the stack is full.
        """
        if self.isFull():
            raise Exception("Stack is Full")
        self.stack.append(val)

    def pop(self):
        """
        Pop the top item off the stack.

        Returns:
            The top item of the stack if the stack is not empty.

        Raises:
            Exception: If the stack is empty.
        """
        if self.isEmpty():
            return None
        endNode = self.stack.pop()
        return endNode.data
    
    def peek(self):
        """
        Peek at the top item of the stack without removing it.

        Returns:
            The top item of the stack if the stack is not empty.

        Raises:
            Exception: If the stack is empty.
        """
        if self.isEmpty():
            return None
        endNode = self.stack.tail
        return endNode.data