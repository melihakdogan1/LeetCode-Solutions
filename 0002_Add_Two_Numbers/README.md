# 0002 · Add Two Numbers

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topics: Linked List, Math](https://img.shields.io/badge/Topics-Linked%20List,%20Math-blue)
[![LeetCode Link](https://img.shields.io/badge/LeetCode-Link-orange)](https://leetcode.com/problems/add-two-numbers/)

---

## Problem

Two non-negative integers are represented as linked lists in **reverse order** (least significant digit first). Return the sum as a linked list in the same format.

**Example:**
```
Input:  l1 = [2,4,3], l2 = [5,6,4]   →   342 + 465
Output: [7,0,8]                        →   807
```

---

## Approach

Traverse both lists simultaneously, digit by digit, while tracking a **carry**.

At each step:
- Add the current digits from both lists plus the carry.
- The new digit is `sum % 10`, the new carry is `sum / 10`.
- Append the new digit to the result list.

The loop continues until both lists are exhausted **and** there is no remaining carry — this naturally handles the case where the final addition produces an extra digit (e.g. 999 + 1 = 1000).

A **dummy head** node is used to simplify list construction, avoiding a special case for the first node.

**Time complexity:** O(max(m, n))  
**Space complexity:** O(max(m, n))

---

## Solutions

### Python

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry, new_digit = divmod(total_sum, 10)

            current.next = ListNode(new_digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
```

### C++

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* current = dummyHead;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;

            current->next = new ListNode(sum % 10);
            current = current->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }
        return dummyHead->next;
    }
};
```
