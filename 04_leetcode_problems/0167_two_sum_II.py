# leetcode -> https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)

        while left<right:
            total = numbers[left-1] + numbers[right-1]
            if total == target:
                return [left, right]
            elif total > target:
                right -= 1
            else:
                left += 1

        return [None, None]