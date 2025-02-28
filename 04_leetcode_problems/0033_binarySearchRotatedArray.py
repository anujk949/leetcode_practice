# leetcode link -> https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        low, high = 0, len(nums)-1

        while high>=low: 
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[low]<=nums[mid]:
                ## sorted array
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid]<=nums[high]:
                ## sorted array
                if nums[mid] <= target <= nums[high]:
                    low = mid +1
                else:
                    high = mid - 1
            

        return -1




        
        