```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: 
                    dp[i][j]=grid[i][j]
                elif i==0 and j!=0: 
                    print(j)
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j==0 and i!=0: 
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
```

