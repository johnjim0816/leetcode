#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-10 14:05:47
@LastEditor: John
@LastEditTime: 2020-05-10 14:06:17
@Discription: 
@Environment: python 3.7.7
'''
# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[0]*(n+1)
        return self.climb_stairs(0,n, memo)
    def climb_stairs(self,i,n,memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i]=self.climb_stairs(i + 1, n,memo) + self.climb_stairs(i + 2, n,memo)
        return memo[i]
        
# @lc code=end

