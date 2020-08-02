#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-16 02:05:31
@LastEditor: John
@LastEditTime: 2020-06-16 02:17:08
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
import operator
class Solution(object):
    def calculate(self, s):
        '''注意，python中-3/2==-2
        '''
        a = []
        opmp = {
            "+": lambda e: a.append(e),
            "-": lambda e: a.append(-e),
            "*": lambda e: a.append(e * a.pop()),
            "/": lambda e: a.append(int(operator.truediv(a.pop(), e)))
        }
        op = "+"
        num = 0
        for c in s+"+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c != " ":
                opmp[op](num)
                op = c
                num = 0
        return sum(a)

        
# @lc code=end

