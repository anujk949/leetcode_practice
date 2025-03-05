# leetcode link -> https://leetcode.com/problems/move-zeroes/description/

from typing import List

# time and space complexity for both the solutions are same O(n), and O(1) respectively

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Iterate over array (nums) as we get any nonzero element at index i, we are planning to swap with zeroIndexAt (which is left of index i)
        if zeroIndexAt and i are same then just pass the loop

        It's like pushing all non zero element on or before zeroIndexAt
        """
        zeroIndexAt = 0

        for i, item in enumerate(nums):
            if item != 0:
                if i == zeroIndexAt:
                    pass
                else:
                    nums[zeroIndexAt], nums[i] = nums[i], nums[zeroIndexAt]
                zeroIndexAt += 1

# using while loop - bit more descriptive where we are checking zero and nonzero indexes both
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = zeroIndex = 0
        
        while (zeroIndex< len(nums)) and (nonZeroIndex < len(nums)):
            if nums[zeroIndex] != 0:
                zeroIndex += 1
                continue

            if nums[nonZeroIndex] == 0:
                nonZeroIndex += 1
                continue

            if nonZeroIndex > zeroIndex:
                nums[nonZeroIndex], nums[zeroIndex] = nums[zeroIndex], nums[nonZeroIndex]
                zeroIndex += 1

            nonZeroIndex += 1

