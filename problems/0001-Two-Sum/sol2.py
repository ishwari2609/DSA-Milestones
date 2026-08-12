# ==========================================================
# 1. Two Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 0 ms (Beats 100%)
# Memory     : 20.6 MB (Beats 7%)
# Link       : https://leetcode.com/problems/two-sum/
# ==========================================================

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

from typing import List