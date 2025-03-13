import pytest
from data_structures import Queue

def test_queue_initialization():
    """
    Test the initialization of an empty queue.
    """
    q = Queue()
    assert q.isEmpty() == True
    assert q.isFull() == False

def test_queue_initialization_with_max_length():
    """
    Test the initialization of a queue with a maximum length.
    """
    q = Queue(max_length=5)
    assert q.isEmpty() == True
    assert q.isFull() == False
    assert q.max_length == 5

def test_enqueue():
    """
    Test enqueuing elements to the queue.
    """
    q = Queue()
    q.enqueue(1)
    assert q.isEmpty() == False
    assert q.peek() == 1

def test_enqueue_full_queue():
    """
    Test enqueuing elements to a full queue.
    """
    q = Queue(max_length=1)
    q.enqueue(1)
    with pytest.raises(Exception, match="Queue is already full"):
        q.enqueue(2)

def test_dequeue():
    """
    Test dequeuing elements from the queue.
    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.peek() == 2

def test_dequeue_empty_queue():
    """
    Test dequeuing elements from an empty queue.
    """
    q = Queue()
    with pytest.raises(Exception, match="No Element Found!"):
        q.dequeue()

def test_peek():
    """
    Test peeking at the front element of the queue.
    """
    q = Queue()
    q.enqueue(1)
    assert q.peek() == 1

def test_peek_empty_queue():
    """
    Test peeking at the front element of an empty queue.
    """
    q = Queue()
    with pytest.raises(Exception, match="No Element Found!"):
        q.peek()