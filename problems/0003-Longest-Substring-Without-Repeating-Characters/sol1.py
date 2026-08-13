# ==========================================================
# 3. Longest Substring Without Repeating Characters
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 220 ms (Beats 15%)
# Memory     : 19.7 MB (Beats 26%)
# Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# ==========================================================

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans