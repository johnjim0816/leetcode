#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-09-05 06:14:08
LastEditor: John
LastEditTime: 2020-09-05 06:14:51
Discription: 
Environment: 
'''
# Source : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Author : JohnJim0816
# Date   : 2020-09-05

##################################################################################################### 
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# Example 1:
# 
# Input: 1->1->2
# Output: 1->2
# 
# Example 2:
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
#####################################################################################################

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