"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        result = min(left_min, right_min) + 1
        return result


class Solution2(object):
    def minDepth(self, root):
        """
        为什么求最大深度时候不需要这么多判断，而最小深度需要增加额外的判断
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left: #如果没有左子树，要找右边的最小情况
            return 1 + self.minDepth(root.right)
        if not root.right: #如果没有右子树，要找左边的最小情况
            return 1 + self.minDepth(root.left)
        # 分治方法，求左边最小值以及右边最小值
        left = self.minDepth(root.left) + 1
        right = self.minDepth(root.right) + 1
        # 需要寻找两边最
        mini = min(left, right)
        return mini

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
    solution = Solution().minDepth(node1)
    print(solution)