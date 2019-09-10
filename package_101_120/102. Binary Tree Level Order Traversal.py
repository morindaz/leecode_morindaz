# -*- coding: utf-8 -*-
# @Time    : 2019/9/10
# @Author  : morindaz
# @FileName: 102. Binary Tree Level Order Traversal.py
# @explanation: This file is for:
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result


    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level +1:
            self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node4.right = node5
    solution = Solution().levelOrder(node1)
    print(solution)

