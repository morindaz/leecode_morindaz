"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # 这里的dp[i]因为随着j不断循环，所以用于记录dp[j]的最大值
            result = max(result, dp[i])
        return result

if __name__ == '__main__':
    solution = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    print(solution)

"""
方法一：采用动态规划，dp[i]表示到达某个数字的最长子序列是多少
状态转移方程是dp[i] = max(dp[j]) + 1 j = 0 ...i-1

方法二：采用二分查找法
找到当前插入数字，替换掉比该数字大的最小的数字，并进行替换
"""