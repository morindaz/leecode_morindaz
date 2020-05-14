# -*- coding: utf-8 -*-
# @Time    : 2020/5/13
# @Author  : morindaz
# @FileName: 239. Sliding Window Maximum.py
# @explanation: This file is for:

"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        采用双端队列的形势
        """
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >=k and window[0] <= i-k:
                window.pop(0) #移除第一个元素
            while window and nums[window[-1]] <= x:
                window.pop() #如果老臣都比新元素小，都移除出去
            window.append(i) #加入新元素
            if i >= k-1:
                res.append(nums[window[0]])
        print(res)
        return res

if __name__ == '__main__':
    solution = Solution()
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    res = solution.maxSlidingWindow(arr, 3)
    print(res)
