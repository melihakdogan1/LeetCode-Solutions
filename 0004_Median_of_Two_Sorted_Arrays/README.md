# 0004 · Median of Two Sorted Arrays

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)
![Topics: Array, Binary Search, Divide and Conquer](https://img.shields.io/badge/Topics-Array,%20Binary%20Search,%20Divide%20and%20Conquer-blue)
[![LeetCode Link](https://img.shields.io/badge/LeetCode-Link-orange)](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## Problem

Given two sorted arrays `nums1` and `nums2`, return the median of the combined array. The solution must run in O(log(m + n)) time.

**Example:**
```
Input:  nums1 = [1,3], nums2 = [2]
Output: 2.0   →   merged: [1,2,3]

Input:  nums1 = [1,2], nums2 = [3,4]
Output: 2.5   →   merged: [1,2,3,4]
```

---

## Approach

Merging both arrays and picking the middle element would be O(m + n) — not good enough. Instead, use **binary search on the partition point**.

The median divides the combined array into two equal halves. The goal is to find a partition in each array such that:
- The left half of `nums1` + left half of `nums2` forms the lower half of the combined array.
- Every element in the left halves is ≤ every element in the right halves.

Binary search is performed on the **smaller array** only, which keeps the complexity at O(log(min(m, n))).

At each step, a `partition1` is chosen for `nums1`, and `partition2` is derived automatically so that both halves together have the correct total size. Then the four boundary values are checked:

- `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1` → valid partition found.
- `maxLeft1 > minRight2` → partition1 is too far right, move `high` left.
- Otherwise → partition1 is too far left, move `low` right.

`INT_MIN` / `INT_MAX` (or `±inf` in Python) handle the edge cases where a partition falls at the start or end of an array.

Once the correct partition is found:
- **Odd** total length → median is `max(maxLeft1, maxLeft2)`.
- **Even** total length → median is the average of the two middle values.

**Time complexity:** O(log(min(m, n)))  
**Space complexity:** O(1)

---

## Solutions

### Python

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            maxLeft1  = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf')  if partition1 == m else nums1[partition1]
            maxLeft2  = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf')  if partition2 == n else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
```

### C++

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);

        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;

        while (low <= high) {
            int partition1 = (low + high) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;

            int maxLeft1  = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];
            int maxLeft2  = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((m + n) % 2 == 0)
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                else
                    return max(maxLeft1, maxLeft2);
            } else if (maxLeft1 > minRight2) {
                high = partition1 - 1;
            } else {
                low = partition1 + 1;
            }
        }
        return 0.0;
    }
};
```
