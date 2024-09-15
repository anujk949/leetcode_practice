Binary Search Algorithm
===


## 1. Key Points
- Binary search algorithms works for **sorted array**.
- Time and Space complexity is O(log n) and O(1) respectively.
- It's possible to use binary search algorithm on unsorted array if a sorted array is rotated. 
- Binary search uses divide and conquer algorithm.
- if we have multiple target value, it is NOT gauranteed that you get index of first element.

    *for example -*
    ```python
    array = [0,1,3,3,4,5,6], target = 3, 
    returns = index = 3 (not 2)
    ``` 
- Do not use binary search when
    * Array is small
    * Dynamic or unsorted array
    * Non contiguous memory type data structure


## 2. Conditions to Apply BS Algorithm
- Array should be sorted *(exceptions -  rotated sorted array)*
- access to any elements of the data structure should takes constant time


## 3. Pseudocode


**Step 1**: Identify the middle element of the sorted array.

```python
# for even number of elements
m = (end + start)/2
# for odd number of elements
m = (end + start - 1)/2
```
we can also use
```python
m = (end + start)//2 #gives integer value
```

**Step 2**: Compare the middle element with the target

- if it is equal to target, return index
- if it is greater than target, choose the left side (i.e. end = mid - 1)
- if it is less than the target, choose the right side (i.e start = mid + 1)

**Step 3**: Break the loop when end is less than start

*Note: The above methos is using `while loop`, there is another method using `recursion`*


## 4. Python Code

```python
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
```

Call the function
```python
bs = BinarySearch()
print(bs.search(arr=[1, 2,2, 4, 6, 9, 10], target=2))
```

## 5. Advantages
- Efficient than linear search O(n) when array is large
- More efficient than other searching algorithms like **interpolation** and **exponential** search with the same time complexity of O(log n)
- Well suited for searching large dataset that are stored externally, like cloud and hard disk.

## 6. Disadvantages
- It requires sorted error, whereas linear search can work on sorted and unsorted array both.
- Data should be there in contiguous memory (all the memory spaces remains together in one place).


## Apllications
- It can be used for searching in Databases
- It is used in building more complex algorithms in machine learning, training neural networks and finding optimal hyper-parameters for a model