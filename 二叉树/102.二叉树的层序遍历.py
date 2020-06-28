#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """广度优先搜索
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque() # 使用队列先进先出
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = [] # 对应深度的所有值
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
        
# @lc code=end

