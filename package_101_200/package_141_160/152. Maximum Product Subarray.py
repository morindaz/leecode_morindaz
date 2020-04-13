"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution(object):
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])
        return res

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cur_min, cur_max, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = cur_max * num, cur_min * num
            cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
            res = max(cur_max, res)
        return res



if __name__ == "__main__":
    solution = Solution().maxProduct([-2,0,-1])
    print(solution)

"""
采用动态规划的思想，第一种方法开一个两维数组，记录最大值最小值，前一次的值以及当前的值
通过模2处理，来变换前一次的值以及当前的值
然后记录下最大值和最小值，乘以当前值
"""