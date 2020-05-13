# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections
class Solution(object):
    """
    广度优先的方法，用queue
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        # visited = set(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level)
        return result


class Solution2(object):
    def levelOrder(self, root):
        if not  root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level + 1: #说明当前行没有任何结果
            self.result.append([])

        self.result[level].append(node.val)
        self._dfs(node.left, level +1)
        self._dfs(node.right, level +1)


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(6)
    e = TreeNode(7)
    f = TreeNode(8)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    solution = Solution()
    result = solution.levelOrder(a)
    print(result)