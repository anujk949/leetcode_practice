from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value: List[int] = []):
        self.head = None
        self.tail = None
        self.length = 0

        if len(value) > 0:
            self.extend(value)

    def __len__(self):
        return self.length

    
    def extend(self, value: List[int]):
        for item in value:
            self.append(item)
            

    def append(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    def prepend(self, data):
        if self.length == 0:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp

        return prev

    def pop(self):
        if self.length == 0:
            raise IndexError("No Element to pop!")
        elif self.length == 1:
            temp = self.tail
            self.head = self.tail = None
            self.length = 0
            return temp
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next

            temp = curr.next
            self.tail = curr
            curr.next = None
            self.length -= 1
            return temp


    def popFirst(self):
        if self.length == 0:
            raise IndexError("No Element to pop!")
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp


    def _get_printable(self, head):
        if head == None:
            return "Linked List is empty"
        curr = head
        ll_str = ""
        while curr.next:
            ll_str += f"{curr.data} -> "
            curr = curr.next
        ll_str += f"{curr.data}"
        return ll_str

    def print(self, head):
        print(self._get_printable(head))

    def __str__(self):
        return self._get_printable(self.head)
