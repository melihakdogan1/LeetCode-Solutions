# 0005 · Longest Palindromic Substring

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topics: String, Dynamic Programming, Manacher's Algorithm](https://img.shields.io/badge/Topics-String,%20DP,%20Manacher's-blue)
[![LeetCode Link](https://img.shields.io/badge/LeetCode-Link-orange)](https://leetcode.com/problems/longest-palindromic-substring/)

---

## Problem

Given a string `s`, return the longest substring that is a palindrome.

**Example:**
```
Input:  s = "babad"
Output: "bab"   (or "aba")

Input:  s = "cbbd"
Output: "bb"
```

---

## Approach — Manacher's Algorithm

The naive approach (expand around every center) is O(n²). Manacher's algorithm solves this in **O(n)** by reusing previously computed palindrome lengths.

**Step 1 — Transform the string**

Insert `#` between every character (and at the ends), plus sentinel characters `^` and `$` at the boundaries:

```
"abc"  →  "^#a#b#c#$"
```

This trick unifies odd and even length palindromes into a single case — every palindrome in the transformed string has odd length. The sentinels eliminate the need for bounds checking in the expansion loop.

**Step 2 — Fill the radius array**

Maintain a `P` array where `P[i]` = radius of the longest palindrome centered at `i` in the transformed string.

Also track the rightmost palindrome boundary (`right`) and its center (`center`). For each new position `i`:

1. If `i` is within the current rightmost boundary, initialize `P[i]` using the mirror position — it can be at least as large as the mirror's radius (capped at the boundary).
2. Try to expand further around `i`.
3. If the new palindrome extends past `right`, update `center` and `right`.

This guarantees each character is visited at most twice total, giving O(n).

**Step 3 — Extract the answer**

Find the index with the maximum `P[i]`. The corresponding start position in the original string is `(centerIndex - maxLen) / 2`.

**Time complexity:** O(n)  
**Space complexity:** O(n)

---

## Solutions

### Python

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            if i < right:
                P[i] = min(right - i, P[2 * center - i])

            while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_len, center_index = max((P[i], i) for i in range(n))
        start = (center_index - max_len) // 2
        return s[start : start + max_len]
```

### C++

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        string t = "^";
        for (char c : s) t += "#" + string(1, c);
        t += "#$";

        int n = t.length();
        vector<int> p(n, 0);
        int center = 0, right = 0;

        for (int i = 1; i < n - 1; i++) {
            int mirror = 2 * center - i;

            if (i < right)
                p[i] = min(right - i, p[mirror]);

            while (t[i + (1 + p[i])] == t[i - (1 + p[i])])
                p[i]++;

            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        int maxLen = 0, centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (p[i] > maxLen) {
                maxLen = p[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2;
        return s.substr(start, maxLen);
    }
};
```
