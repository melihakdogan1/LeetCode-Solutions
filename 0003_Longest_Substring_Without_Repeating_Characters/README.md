# 0003 · Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Topics:** String, Sliding Window, Hash Table

---

## Problem

Given a string `s`, return the length of the longest substring that contains no repeating characters.

**Example:**
```
Input:  s = "abcabcbb"
Output: 3   →   "abc"

Input:  s = "pwwkew"
Output: 3   →   "wke"
```

---

## Approach

**Sliding window** with a map that tracks the last seen index of each character.

Two pointers, `left` and `right`, define the current window. As `right` advances:
- If the current character was seen before **and** its last position falls within the current window (`>= left`), move `left` to one past that position — effectively evicting the duplicate.
- Update the character's last seen index.
- Update the maximum length.

The `>= left` check is important: a character may exist in the map from a previous window that has already been passed. In that case `left` should not move backwards.

**Time complexity:** O(n)  
**Space complexity:** O(1) — the map is bounded by the character set size (128 for ASCII)

---

## Solutions

### Python

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
```

### C++

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> char_map(128, -1);
        int left = 0;
        int max_len = 0;
        int n = s.length();

        for (int right = 0; right < n; right++) {
            char current_char = s[right];

            if (char_map[current_char] >= left) {
                left = char_map[current_char] + 1;
            }
            char_map[current_char] = right;

            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
```

> The C++ solution uses a fixed-size array indexed by ASCII value instead of a hash map, which avoids hashing overhead entirely.
