



```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                res+=1
            mask <<= 1
        return res
```

