import pytest
from data_structures import StackList

# filepath: d:\git_dir\leetcode_practice\data_structures\test_stack.py

def test_stack_initialization():
    """
    Test the initialization of an empty stack.
    """
    stack = StackList()
    assert stack.size() == 0
    assert stack.is_empty() == True
    assert stack.is_full() == False

def test_stack_initialization_with_max_length():
    """
    Test the initialization of a stack with a maximum length.
    """
    stack = StackList(max_length=5)
    assert stack.size() == 0
    assert stack.is_empty() == True
    assert stack.is_full() == False
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

def test_is_empty():
    """
    Test checking if the stack is empty.
    """
    stack = StackList()
    assert stack.is_empty() == True

    stack.push(1)
    assert stack.is_empty() == False

def test_is_full():
    """
    Test checking if the stack is full.
    """
    stack = StackList(max_length=1)
    assert stack.is_full() == False

    stack.push(1)
    assert stack.is_full() == True