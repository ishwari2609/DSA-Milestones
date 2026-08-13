# ==========================================================
# 3. Longest Substring Without Repeating Characters
# Difficulty : Medium
# Language   : Python
# Solution   : #3
# Runtime    : 204 ms (Beats 23%)
# Memory     : 19.9 MB (Beats 21%)
# Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# ==========================================================

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        ans = 0
        left = 0
        seen = set()
    def lengthOfLongestSubstring(self, s: str) -> int:
class Solution: