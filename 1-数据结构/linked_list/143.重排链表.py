#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-05 08:57:41
@LastEditor: John
@LastEditTime: 2020-07-05 09:53:12
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
        
# @lc code=end

