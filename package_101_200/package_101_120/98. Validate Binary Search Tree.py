"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        第一种思路，采用中序遍历的方式，看是否是升序
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        tmp = self.inorder(root.left) + [root.val] + self.inorder(root.right)
        return tmp

class Solution2(object):
    def isValidBST(self, root):
        """
        还没有调试过，不用保存整个遍历的数组，只要保存大小关系就可以
        :param root:
        :return:
        """
        self.prev = None
        return self.helper(root)


    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

class Solution3(object):
    def isValidBST(self, root):
        # 采用中序遍历方法，判断是不是和排序后结果一样
        inorder_result = self.inorder(root)
        print(inorder_result)
        return inorder_result == list(sorted(set(inorder_result))) #必须要加set,否则[1,1]这个情况判断错误

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 =TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(3)
    node5 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    solution = Solution3().isValidBST(node1)
    print(solution)