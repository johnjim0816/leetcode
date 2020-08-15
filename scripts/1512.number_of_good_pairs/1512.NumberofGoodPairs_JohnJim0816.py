#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-08-15 11:02:58
LastEditor: John
LastEditTime: 2020-08-15 11:03:11
Discription: 
Environment: 
'''
# Source : https://leetcode.com/problems/number-of-good-pairs/
# Author : JohnJim0816
# Date   : 2020-08-15

##################################################################################################### 
#
# Given an array of integers nums.
# 
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# 
# Return the number of good pairs.
# 
# Example 1:
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# 
# Example 2:
# 
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# 
# Example 3:
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# Constraints:
# 
# 	1 <= nums.length <= 100
# 	1 <= nums[i] <= 100
#####################################################################################################

class Solution:
    '''哈希表+组合计数
    '''
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())