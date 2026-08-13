# ==========================================================
# 4. Median of Two Sorted Arrays
# Difficulty : Hard
# Language   : Python
# Solution   : #1
# Runtime    : 2 ms (Beats 51%)
# Memory     : 19.5 MB (Beats 77%)
# Link       : https://leetcode.com/problems/median-of-two-sorted-arrays/
# ==========================================================

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) //2 - partition1 

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]