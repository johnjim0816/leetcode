#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-31 10:03:59
@LastEditor: John
@LastEditTime: 2020-05-31 10:04:04
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while right>left:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]: # nums[mid]处于局部升序,left右移
                left=mid+1
            else: # 若处于降序(依题不会出现平序)，则指针right左移
                right=mid
        return mid
# @lc code=end

