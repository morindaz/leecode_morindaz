"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m +1)]
        for i in range(m + 1): dp[i][0] = i
        for j in range(n + 1): dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j] + 1,
                               dp[i][j-1] + 1)
        return dp[m][n]


    def minDistance1(self, word1, word2):
        pass




if __name__ == '__main__':
    solution = Solution().minDistance("AV","VA")
    print(solution)
"""
编辑距离
思路一：暴力法 通过dfs或者bfs
思路二：动态规划，状态定义以及状态转移
dp[i][j] i单词1的前i个字符 j单词2的前j个字符
word1的前i个字符 替换掉word2的前j个字符 至少需要多少步数
操作，增加、删除、替换
如果w1[i] == w2[j]
dp[i,j] = dp[i-1,j-1]
否则
a + min(dp[i-1,j], dp[i,j-1], dp[i-1,j-1])
"""