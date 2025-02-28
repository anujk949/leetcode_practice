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


    def __str__(self):
        if self.length == 0:
            return "Linked List is empty"
        curr = self.head
        ll_str = ""
        while curr.next:
            ll_str += f"{curr.data} -> "
            curr = curr.next
        ll_str += f"{curr.data}"
        return ll_str

if __name__ == "__main__":
    ll = LinkedList([1,2])
    ll.extend([3,4,5])
    print(len(ll))
