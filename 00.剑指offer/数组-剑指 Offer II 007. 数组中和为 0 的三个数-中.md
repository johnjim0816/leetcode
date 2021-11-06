####[剑指 Offer II 007. 数组中和为 0 的三个数](https://leetcode-cn.com/problems/1fGaJU/)



```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # if nums[i] > 0:
            #     break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    val = nums[left]
                    while left < right and nums[left] == val:
                        left += 1
                elif tmp > 0:
                    right -= 1
                else:
                    left += 1
        return res

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/1fGaJU/solution/shua-chuan-jian-zhi-offer-day05-shu-zu-i-e2af/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

