#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-29 10:03:41
@LastEditor: John
@LastEditTime: 2020-06-30 09:26:32
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None) # 虚拟头结点
        dummy_head.next = head

        pre = dummy_head
        cur = head

        while cur:
            if pre and cur.val == pre.val:
                pre.next = cur.next
                cur.next = None # 清除野指针
                cur = pre.next
                continue

            pre = cur
            cur = cur.next
        return dummy_head.next
# @lc code=end

