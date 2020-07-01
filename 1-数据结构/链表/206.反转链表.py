#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-01 09:38:24
@LastEditor: John
@LastEditTime: 2020-07-01 09:51:11
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''双指针(pre,cur)迭代
        '''
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            # cur下一个结点指向pre
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
# @lc code=end

