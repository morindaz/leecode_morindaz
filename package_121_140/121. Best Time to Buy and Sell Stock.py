"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        min_price = prices[0]
        max_profit = 0
        for price in range(1, len(prices)):
            max_profit = max(max_profit, prices[price] - min_price)
            min_price = min(min_price, prices[price])
        return max_profit



if __name__ == '__main__':
    solution = Solution().maxProfit([7,1,5,3,6,4])
    print(solution)

"""
动态规划买卖股票
121/122/123/309/188/714
"""