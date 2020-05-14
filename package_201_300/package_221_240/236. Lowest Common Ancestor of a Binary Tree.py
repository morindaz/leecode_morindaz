# -*- coding: utf-8 -*-
# @Time    : 2020/5/14
# @Author  : morindaz
# @FileName: 236. Lowest Common Ancestor of a Binary Tree.py
# @explanation: This file is for:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root #如果没有根节点或者根节点等于待查的值，根节点就是公共父节点
        # 分治操作
        left = self.lowestCommonAncestor(root.left, p, q) #到左子树找p,q的值
        right = self.lowestCommonAncestor(root.right, p, q) #到右子树找p,q的值
        if not right: #如果没有在右子树里面找到，也就是p,q都在左子树中
            return left #说明最近祖先在左子树
        elif not left: #如果没有在左子树找到，也就是p,q都在右子树中
            return right #说明最近祖先在右子树
        else:
            return root #否则左右子树都找到了，说明当前节点就是最近祖先



if __name__ == '__main__':
    a1 = TreeNode(6)
    a2 = TreeNode(2)
    a3 = TreeNode(8)
    a4 = TreeNode(0)
    a5 = TreeNode(4)
    a6 = TreeNode(7)
    a7 = TreeNode(9)
    a8 = TreeNode(3)
    a9 = TreeNode(5)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7
    a5.left = a8
    a5.right = a9
    solution = Solution()
    res = solution.lowestCommonAncestor(a1, a8, a7)
    print(res)