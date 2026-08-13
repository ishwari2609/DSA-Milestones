<div align="center">

# 3. Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffa116?style=for-the-badge&labelColor=1a1a2e)  ![Language](https://img.shields.io/badge/Language-Python-6c5ce7?style=for-the-badge&labelColor=1a1a2e&logo=code)  ![Solutions](https://img.shields.io/badge/Solutions-3-6c5ce7?style=for-the-badge&labelColor=1a1a2e)  ![Date](https://img.shields.io/badge/Date-2026-08-13-0984e3?style=for-the-badge&labelColor=1a1a2e)

[![LeetCode](https://img.shields.io/badge/View%20on-LeetCode-ffa116?style=flat-square&logo=leetcode&logoColor=ffa116)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

</div>

---

## 🏷️ Topics

`Hash Table` `String` `Sliding Window`

## 🏆 Best Performance

| Metric | This Attempt | All-time Best |
|--------|:-----------:|:------------:|
| ⚡ Runtime | 204 ms (Beats 23%) | **204 ms (Beats 23%)** 🆕 |
| 💾 Memory  | 19.9 MB (Beats 21%) | **19.9 MB (Beats 21%)** |

> 🎉 **New personal best!** Runtime improved!

## 💡 Solutions (3 total)

| # | File | Language | Date |
|:-:|------|:--------:|:----:|
| 1 | [sol1.py](./sol1.py) | `Python` | 2026-08-13 |
| 2 | [sol2.py](./sol2.py) | `Python` | 2026-08-13 |
| 3 | [sol3.py](./sol3.py) | `Python` | 2026-08-13 ← **latest** |

---

## 📋 Problem Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

**Example 1:**

```

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

```

**Example 2:**

```

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

```

**Example 3:**

```

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

**Constraints:**

	- `0 <= s.length <= 10^5`

	- `s` consists of English letters, digits, symbols and spaces.

---

<p align="right">
  <sub>🤖 Auto-pushed by <a href="https://deveshsamant.in/">Devesh Samant</a>'s <strong>LeetSync</strong> extension</sub>
</p>
