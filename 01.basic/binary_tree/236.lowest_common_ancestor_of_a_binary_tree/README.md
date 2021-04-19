# [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

最近公共祖先的定义： 设节点 root 为节点 p, q的某公共祖先，若其左子节点root.left和右子节点 root.right 都不是 p,q的公共祖先，则称 root是 “最近的公共祖先” 。

根据以上定义，若 root是 p, q的 最近公共祖先 ，则只可能为以下情况之一：

* p 和 q 在 root的子树中，且分列 root的 异侧（即分别在左、右子树中）;
* p = root ，且 q 在 root 的左或右子树中；
* q = root ，且 p 在 root 的左或右子树中；

**递归解析**：

**终止条件**：

当越过叶节点，则直接返回 null ；
当 root 等于 p, q ，则直接返回 root ；

**递推工作**：

开启递归左子节点，返回值记为 left ；
开启递归右子节点，返回值记为 right ；

**返回值**： 

根据 left 和 right，可展开为四种情况；

当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q，返回 null ；

当 left 和 right 同时不为空 ：说明 p, q分列在 root 的 异侧 （分别在 左 / 右子树），因此 root为最近公共祖先，返回 root ；

当 left为空 ，right 不为空 ：p,q都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：

p,q其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p）；

p,q 两节点都在 root 的 右子树 中，此时的 right指向 最近公共祖先节点 ；
当 left 不为空 ， right 为空 ：与情况 3. 同理；





