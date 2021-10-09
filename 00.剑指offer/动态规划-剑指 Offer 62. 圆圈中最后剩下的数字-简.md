#### [剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

```python
class Solution:
    '''
    f(n,m):n个元素每隔m个数删后最后剩下的那个数的索引
    f(n,m) = f(n-1,m) + m 如果溢出超过n,则对n取余
    '''
    def lastRemaining(self, n: int, m: int) -> int:
        dp = 0
        for i in range(2,n+1):
            dp = (dp+m)%i
        return dp

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/jian-zhi-offer-62-yuan-quan-zhong-zui-ho-dcow/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

