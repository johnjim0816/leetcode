#### [剑指 Offer II 009. 乘积小于 K 的子数组](https://leetcode-cn.com/problems/ZVAVXX/)



```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        left = res = 0
        tmp = 1
        for right, num in enumerate(nums):
            tmp *= num
            while left <= right and tmp >= k:
                tmp //= nums[left]
                left += 1
            res += right - left + 1
        return res

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/ZVAVXX/solution/jian-zhi-offerii009cheng-ji-xiao-yu-kde-q158e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

