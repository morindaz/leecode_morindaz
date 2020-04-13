"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute

the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [amount + 1 for _ in range(amount + 1)]
        result[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    result[i] = min(result[i], result[i - coins[j]] + 1)
        if result[amount] > amount:
            return -1
        else:
            return result[amount]

if __name__ == '__main__':
    solution = Solution().coinChange([1,2,5], 11)
    print(solution)

"""
交换硬币

思路一：深度优先搜索
思路二：动态规划的思想
开一个数组存储到达每个金额需要的最小步数，需要金额数量+1的长度，因为第一个是金额为0的情况

"""