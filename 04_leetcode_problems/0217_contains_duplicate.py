## leetcode link -> https://leetcode.com/problems/contains-duplicate/description/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for item in nums:
            if item in seen:
                return True
            seen.add(item)

        return False