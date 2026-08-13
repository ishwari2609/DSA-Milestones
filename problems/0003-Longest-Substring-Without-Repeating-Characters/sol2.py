# ==========================================================
# 3. Longest Substring Without Repeating Characters
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 211 ms (Beats 20%)
# Memory     : 20.1 MB (Beats 10%)
# Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# ==========================================================

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans