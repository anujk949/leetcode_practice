import pytest
from data_structures import StackList
from data_structures import StackUsingLinkedList

# filepath: d:\git_dir\leetcode_practice\data_structures\test_stack.py

def test_stack_initialization():
    """
    Test the initialization of an empty stack.
    """
    stack = StackList()
    assert stack.size() == 0
    assert stack.isEmpty() == True
    assert stack.isFull() == False

def test_stack_initialization_with_max_length():
    """
    Test the initialization of a stack with a maximum length.
    """
    stack = StackList(max_length=5)
    assert stack.size() == 0
    assert stack.isEmpty() == True
    assert stack.isFull() == False
    assert stack.max_length == 5

def test_push():
    """
    Test pushing elements onto the stack.
    """
    stack = StackList()
    stack.push(1)
    assert stack.size() == 1
    assert stack.peek() == 1

    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2

def test_push_full_stack():
    """
    Test pushing elements onto a full stack.
    """
    stack = StackList(max_length=1)
    stack.push(1)
    with pytest.raises(Exception, match="Stack is full"):
        stack.push(2)

def test_pop():
    """
    Test popping elements from the stack.
    """
    stack = StackList()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.peek() == 1

    assert stack.pop() == 1
    assert stack.size() == 0
    assert stack.peek() == None

def test_pop_empty_stack():
    """
    Test popping elements from an empty stack.
    """
    stack = StackList()
    assert stack.pop() == None

def test_peek():
    """
    Test peeking at the top element of the stack.
    """
    stack = StackList()
    stack.push(1)
    assert stack.peek() == 1

    stack.push(2)
    assert stack.peek() == 2

def test_peek_empty_stack():
    """
    Test peeking at the top element of an empty stack.
    """
    stack = StackList()
    assert stack.peek() == None

def test_isEmpty():
    """
    Test checking if the stack is empty.
    """
    stack = StackList()
    assert stack.isEmpty() == True

    stack.push(1)
    assert stack.isEmpty() == False

def test_isFull():
    """
    Test checking if the stack is full.
    """
    stack = StackList(max_length=1)
    assert stack.isFull() == False

    stack.push(1)
    assert stack.isFull() == True


def test_stack_linkedlist_initialization():
    """
    Test the initialization of an empty stack using linked list.
    """
    stack = StackUsingLinkedList()
    assert stack.size() == 0
    assert stack.isEmpty() == True
    assert stack.isFull() == False

def test_stack_linkedlist_initialization_with_max_length():
    """
    Test the initialization of a stack using linked list with a maximum length.
    """
    stack = StackUsingLinkedList(max_length=5)
    assert stack.size() == 0
    assert stack.isEmpty() == True
    assert stack.isFull() == False
    assert stack.max_length == 5

def test_stack_linkedlist_push():
    """
    Test pushing elements onto the stack using linked list.
    """
    stack = StackUsingLinkedList()
    stack.push(1)
    assert stack.size() == 1
    assert stack.peek() == 1

    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2

def test_stack_linkedlist_push_full_stack():
    """
    Test pushing elements onto a full stack using linked list.
    """
    stack = StackUsingLinkedList(max_length=1)
    stack.push(1)
    with pytest.raises(Exception, match="Stack is Full"):
        stack.push(2)

def test_stack_linkedlist_pop():
    """
    Test popping elements from the stack using linked list.
    """
    stack = StackUsingLinkedList()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.peek() == 1

    assert stack.pop() == 1
    assert stack.size() == 0
    assert stack.peek() == None

def test_stack_linkedlist_pop_empty_stack():
    """
    Test popping elements from an empty stack using linked list.
    """
    stack = StackUsingLinkedList()
    assert stack.pop() == None

def test_stack_linkedlist_peek():
    """
    Test peeking at the top element of the stack using linked list.
    """
    stack = StackUsingLinkedList()
    stack.push(1)
    assert stack.peek() == 1

    stack.push(2)
    assert stack.peek() == 2

def test_stack_linkedlist_peek_empty_stack():
    """
    Test peeking at the top element of an empty stack using linked list.
    """
    stack = StackUsingLinkedList()
    assert stack.peek() == None

def test_stack_linkedlist_isEmpty():
    """
    Test checking if the stack using linked list is empty.
    """
    stack = StackUsingLinkedList()
    assert stack.isEmpty() == True

    stack.push(1)
    assert stack.isEmpty() == False

def test_stack_linkedlist_isFull():
    """
    Test checking if the stack using linked list is full.
    """
    stack = StackUsingLinkedList(max_length=1)
    assert stack.isFull() == False