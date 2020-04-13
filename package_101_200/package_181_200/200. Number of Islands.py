"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
import collections

class Solution(object):
    def __init__(self):
        self.dx = [-1, 1, 0, 0] #上下左右
        self.dy = [0, 0, -1, 1]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return
        self.max_x = len(grid) #总共多少行0
        self.max_y = len(grid[0]) #总共多少列
        self.grid = grid
        self.visited = set() #存放访问过的节点坐标
        return sum([self.floodfill_DFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def flood_BFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x,y))
        queue = collections.deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                new_x, new_y = cur_x + self.dx[i], cur_y + dy[i]
                if self._is_valid(new_x, new_y):
                    self.visited.add(new_x, new_y)
                    queue.append((new_x, new_y))


    def floodfill_DFS(self, x, y):
        if not self._is_valid(x, y): #对当前节点判断是否合理
            return 0
        self.visited.add((x, y)) # 加上节点访问过了
        for k in range(4):
            if x + self.dx[k] <self.max_x and  y + self.dy[k] < self.max_y:
                self.floodfill_DFS(x + self.dx[k], y + self.dy[k])
        return 1

    def _is_valid(self, x, y):
        if x <0 or x > self.max_x or y < 0 or y > self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x,y) in self.visited):
            return False
        return True


if __name__ == '__main__':
    arr = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]

    arr2 =[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

    arr1 = [["11000"],
            ["11000"],
            ["00100"],
            ["00011"]]
    solution = Solution().numIslands(arr2)
    print(solution)