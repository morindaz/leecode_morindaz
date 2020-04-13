"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        mini = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = triangle[i][j] + min(mini[j], mini[j+1])
        return mini[0]


class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        mini = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                mini[j] = min(mini[j], mini[j+1]) + triangle[i][j]
        return mini[0]

if __name__ == "__main__":
    solution = Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
    print(solution)

"""
采用动态规划的思想，从最后一层开始推导，利用递推公式
将mini数据作为中间变量节省空间，核心思想就是重复的利用这个数组，可以从中取数
"""