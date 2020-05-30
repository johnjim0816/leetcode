#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-30 23:54:18
@LastEditor: John
@LastEditTime: 2020-05-31 00:00:16
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # 矩阵行数
        if m == 0:
            return False
        n = len(matrix[0]) # 矩阵列数
        
        #二分查找
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2 # ”//“表示向下取整的除法
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False

# @lc code=end

