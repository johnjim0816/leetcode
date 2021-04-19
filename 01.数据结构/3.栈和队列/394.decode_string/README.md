# [394. Decode String](https://leetcode.com/problems/decode-string/)

有点类似于前缀表达式

## 辅助栈法

考虑3[a2[b]]等嵌套情况用栈最方便，然后需要考虑连续整数出现的情况如32[a]

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi*10+int(c)  # 可能出现连续数字需要*10         
            else:
                res += c
        return res
```

## 递归法

## Refs

https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

