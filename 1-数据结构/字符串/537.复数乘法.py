#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-19 20:59:32
@LastEditor: John
@LastEditTime: 2020-06-19 21:10:07
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a[:-1]        
        b = b[:-1]
        
        # 以+号为界分开
        a = list(map(int, a.split('+')))
        b = list(map(int, b.split('+')))
        
        re = a[0] * b[0] - a[1] * b[1]
        im = a[0] * b[1] + a[1] * b[0]
        
        re = str(re)
        im = str(im)
        
        res = re + '+' + im + 'i'
        return res

# @lc code=end

