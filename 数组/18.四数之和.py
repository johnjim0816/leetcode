#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-11 17:56:24
@LastEditor: John
@LastEditTime: 2020-05-21 16:45:36
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b+1
                d = len(nums)-1
                while c < d:
                    sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if sum == target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        while c<d and nums[c] == nums[c+1]:
                            c += 1
                        while c<d and nums[d] == nums[d-1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif sum < target:
                        c += 1
                    else:
                        d -= 1
        return res
# @lc code=end

