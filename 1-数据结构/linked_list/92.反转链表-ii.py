#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-01 10:03:52
@LastEditor: John
@LastEditTime: 2020-07-01 10:37:41
@Discription: 
@Environment: python 3.7.7
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        ''' 迭代
        '''
        # 判断链表是否为空
        if not head:
            return None
        cur, pre = head, None
        # 先移动到需要反转的开头
        while m > 1:
            pre = cur
            cur = cur.next
            m, n = m-1, n-1
        # tail将是反转部分的尾结点，也是原链表第m个结点。con将是反转部分的前一个结点，即第m-1个结点后面要连接起来
        tail, con = cur, pre
        # 反转m，n之间的结点，跟92题一样
        while n:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1
        # 此时cur是第n+1个结点，pre是原先的第n个点，现在需要将con.next连到pre，tail.next连到cur

        # 考虑到m=1是con将是假的空结点，因此需要判断
        if con:
            con.next = pre
        else:
            head = pre

        tail.next = cur
        return head
# @lc code=end
