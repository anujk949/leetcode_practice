import pytest

class BinarySearch:
    def __init__(self):
        pass


    def search(self, arr:list, target:int) -> int:
        start = 0
        end = len(arr) - 1

        while end >= start:
            ## calculate mid value
            # if value is odd automatically because of integer division it will give root value
            mid = (end+start)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
    

### test cases ###

bs = BinarySearch()

def test_1():
    assert(bs.search(arr=[], target=2) == -1)

def test_2():
    assert(bs.search(arr=[-3, -1 , 0, 1, 3, 5, 7, 89], target=-1) == 1)

def test_3():
    assert(bs.search(arr=[0,2,3,6,9,41,57], target=57) == 6)


def test_4():
    assert(bs.search(arr=[2], target=2) == 0)

def test_5():
    assert(bs.search(arr=[1, 2,2, 4, 6, 9, 10], target=2) in [1,2])
        