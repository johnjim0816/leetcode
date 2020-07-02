#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-02 09:04:26
@LastEditor: John
@LastEditTime: 2020-07-02 09:09:29
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # left 和 right是分割后左右链表的指针， left_head用于返回值，right_head是右链表的头结点，用于后面的拼接
        left = left_head= ListNode(0)
        right = right_head = ListNode(0)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next =head
                right=right.next
            head = head.next
        right.next = None # 清除野指针
        left.next = right_head.next
        return left_head.next
        
# @lc code=end

