# 0001 · Two Sum

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics: Array, Hash Table](https://img.shields.io/badge/Topics-Array,%20Hash%20Table-blue)
[![LeetCode Link](https://img.shields.io/badge/LeetCode-Link-orange)](https://leetcode.com/problems/two-sum/)

---

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and the same element may not be used twice.

**Example:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

---

## Approach

Instead of checking every pair (brute force O(n²)), a single pass through the array is enough.

For each element, calculate its **complement** (`target - nums[i]`) and look it up in a hash map. If the complement exists, the answer is found. If not, store the current element and its index before moving on.

This works because any valid pair will be detected when the second element is reached — the first element is already in the map by then.

**Time complexity:** O(n)  
**Space complexity:** O(n)

---

## Solutions

### Python

```python
class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[num] = i

        return []
```

### C++

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            auto it = seen.find(complement);
            if (it != seen.end()) {
                return {it->second, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
```
