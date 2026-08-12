# ==========================================================
# 1. Two Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 20.5 MB (Beats 18%)
# Link       : https://leetcode.com/problems/two-sum/
# ==========================================================

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

        seen = {}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
from typing import List