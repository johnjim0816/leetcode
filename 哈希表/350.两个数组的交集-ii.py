#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-02 11:10:38
@LastEditor: John
@LastEditTime: 2020-06-02 13:04:03
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        num1_map = {}
        for num in nums1:
            num1_map[num] = num1_map.get(num, 0) + 1
        res = []
        for num in nums2:
            if num1_map.get(num, 0) > 0:
                res.append(num)
                num1_map[num] -= 1
        return res
# @lc code=end

