#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 如果head或head.next都是None，则直接返回
        if not (head and head.next):
            return head
        cur, length = head,0 # cur指针
        # 求链表长度
        while cur:
            cur,length=cur.next,length+1
        ans = ListNode(0) # 定义虚拟结点
        ans.next= head
        intv =1 # 每次合并的规模
        while intv<length:
            merge_point, cur = ans, ans.next
            while cur:
                # 获取当前需要归并的子链表h1
                h1,intv1=cur,intv
                while intv1 and cur:
                    cur,intv1=cur.next,intv1-1
                if intv1: # h2 在这种情况下不存在，所以本轮不需要合并
                    break
                # 获取当前需要归并的子链表h2
                h2,intv2=cur,intv
                while intv2 and cur:
                    cur,intv2=cur.next,intv2-1
                len1,len2=intv,intv-intv2   # len2 的长度可能比intv小
                while len1 and len2:  # 归并排序
                    if h1.val < h2.val: 
                        merge_point.next, h1, len1 = h1, h1.next, len1 - 1
                    else: 
                        merge_point.next, h2, len2 = h2, h2.next, len2 - 1
                    merge_point = merge_point.next
                if len1:              # 归并排序处理一下没有被归并的剩余值
                     merge_point.next = h1  
                else:
                    merge_point.next = h2
                while len1 > 0 or len2 > 0: 
                    merge_point, len1, len2 = merge_point.next, len1 - 1, len2 - 1

                merge_point.next = cur  # h1 和 h2 的归并只是影响了链表的一部分，这里应该把归并后的链表切片跟原链表h2之后的部分拼起来
            intv *= 2
        return ans.next
# @lc code=end

