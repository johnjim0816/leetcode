#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-11 11:14:10
@LastEditor: John
@LastEditTime: 2020-05-11 11:29:00
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''一遍哈希表
        '''
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num),i]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


        
# @lc code=end

