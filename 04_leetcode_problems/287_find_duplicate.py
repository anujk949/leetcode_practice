# Link: https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

# this problem behaves like linked list cycle detection
# we can use the floyd's tortoise and hare algorithm

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        # find the intersetion point of the two runners
        # this is the cycle in the linked list
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # find the "entrance" to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow