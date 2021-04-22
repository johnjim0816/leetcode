# [剑指 Offer 24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/shi-pin-tu-jie-jian-zhi-offer-24-fan-zhu-oym7/

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
```

