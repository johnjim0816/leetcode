#### [剑指 Offer II 012. 左右两边子数组的和相等](https://leetcode-cn.com/problems/tvdfij/)

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        presum = [0 for _ in range(n + 1)]
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        
        for i in range(n):
            l = presum[i]
            r = presum[n] - presum[i+1]
            if l == r:
                return i
        
        return -1

# 作者：Hanxin_Hanxin
# 链接：https://leetcode-cn.com/problems/tvdfij/solution/cpython3java-qian-zhui-he-by-hanxin_hanx-jqji/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

