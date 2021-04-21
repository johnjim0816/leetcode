
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

典型问题比如八皇后问题，常见于深度优先搜索中。
[五大常用算法之四：回溯法](https://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741376.html)

## Refs

[回溯算法解题套路框架](https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban)