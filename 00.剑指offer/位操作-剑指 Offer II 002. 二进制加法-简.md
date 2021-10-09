#### [剑指 Offer II 002. 二进制加法](https://leetcode-cn.com/problems/JFETK5/)



跟[剑指 Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)一样，少了大数越界问题

```python
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2) # 二进制转十进制
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/JFETK5/solution/er-jin-zhi-jia-fa-by-leetcode-solution-fa6t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

