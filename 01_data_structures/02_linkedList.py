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

    def __get_printable(self, head):
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
        print(self.__get_printable(head))

    def __str__(self):
        return self.__get_printable(self.head)


if __name__ == "__main__":
    ll = LinkedList()
    ll.extend([3,4,5])
    ll.prepend(0)
    ll.append(6)
    
    print(ll)
    ll.print(ll.reverse())
