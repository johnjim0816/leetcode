#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-09-05 06:16:22
LastEditor: John
LastEditTime: 2020-09-05 06:16:48
Discription: 
Environment: 
'''
# Source : https://leetcode.com/problems/reorder-list/
# Author : JohnJim0816
# Date   : 2020-09-05

##################################################################################################### 
#
# Given a singly linked list L: L0&rarr;L1&rarr;&hellip;&rarr;Ln-1&rarr;Ln,
# reorder it to: L0&rarr;Ln&rarr;L1&rarr;Ln-1&rarr;L2&rarr;Ln-2&rarr;&hellip;
# 
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
# Example 1:
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
#####################################################################################################

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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 如果head或head.next 都是None，则直接返回

        if not (head and head.next):
            return head
        # 利用快慢指针找到中点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p2 = slow.next # 翻转头
        slow.next = None # 切断链表头后半部分
        p2 = self.reverseList(p2)
        p1 = head
        while p2:
            # 拼接
            p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next