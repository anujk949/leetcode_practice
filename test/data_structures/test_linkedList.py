import pytest
from data_structures import LinkedList

def test_linked_list_initialization():
    """
    Test the initialization of an empty linked list.
    """
    ll = LinkedList()
    assert len(ll) == 0
    assert ll.head == None
    assert ll.tail == None

def test_linked_list_initialization_with_values():
    """
    Test the initialization of a linked list with initial values.
    """
    ll = LinkedList([1, 2, 3])
    assert len(ll) == 3
    assert ll.head.data == 1
    assert ll.tail.data == 3

def test_append():
    """
    Test appending elements to the linked list.
    """
    ll = LinkedList()
    ll.append(1)
    assert len(ll) == 1
    assert ll.head.data == 1
    assert ll.tail.data == 1

    ll.append(2)
    assert len(ll) == 2
    assert ll.head.data == 1
    assert ll.tail.data == 2

def test_prepend():
    """
    Test prepending elements to the linked list.
    """
    ll = LinkedList()
    ll.prepend(1)
    assert len(ll) == 1
    assert ll.head.data == 1
    assert ll.tail.data == 1

    ll.prepend(2)
    assert len(ll) == 2
    assert ll.head.data == 2
    assert ll.tail.data == 1

def test_pop():
    """
    Test popping elements from the end of the linked list.
    """
    ll = LinkedList([1, 2, 3])
    node = ll.pop()
    assert node.data == 3
    assert len(ll) == 2
    assert ll.tail.data == 2

    node = ll.pop()
    assert node.data == 2
    assert len(ll) == 1
    assert ll.tail.data == 1

    node = ll.pop()
    assert node.data == 1
    assert len(ll) == 0
    assert ll.head == None
    assert ll.tail == None

    with pytest.raises(IndexError, match="No Element to pop!"):
        ll.pop()

def test_pop_first():
    """
    Test popping elements from the beginning of the linked list.
    """
    ll = LinkedList([1, 2, 3])
    node = ll.popFirst()
    assert node.data == 1
    assert len(ll) == 2
    assert ll.head.data == 2

    node = ll.popFirst()
    assert node.data == 2
    assert len(ll) == 1
    assert ll.head.data == 3

    node = ll.popFirst()
    assert node.data == 3
    assert len(ll) == 0
    assert ll.head == None
    assert ll.tail == None

    with pytest.raises(IndexError, match="No Element to pop!"):
        ll.popFirst()

def test_reverse():
    """
    Test reversing the linked list.
    """
    ll = LinkedList([1, 2, 3])
    reversed_head = ll.reverse()
    assert reversed_head.data == 3
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 1
    assert reversed_head.next.next.next == None

def test_extend():
    """
    Test extending the linked list with multiple elements.
    """
    ll = LinkedList()
    ll.extend([1, 2, 3])
    assert len(ll) == 3
    assert ll.head.data == 1
    assert ll.tail.data == 3

def test_str():
    """
    Test the string representation of the linked list.
    """
    ll = LinkedList([1, 2, 3])
    assert str(ll) == "1 -> 2 -> 3"
    ll = LinkedList()
    assert str(ll) == "Linked List is empty"