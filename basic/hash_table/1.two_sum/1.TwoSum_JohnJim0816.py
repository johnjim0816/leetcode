#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-08-15 11:06:28
LastEditor: John
LastEditTime: 2020-08-15 11:06:42
Discription: 
Environment: 
'''
# Source : https://leetcode.com/problems/two-sum/
# Author : JohnJim0816
# Date   : 2020-08-15

##################################################################################################### 
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific 
# target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same 
# element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
#####################################################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''两遍哈希表
        '''
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
