# -*- coding: utf-8 -*-
# @Time    : 2019/10/29
# @Author  : morindaz
# @FileName: 53..py
# @explanation: This file is for:

"""
53. Maximum Subarray
Easy

5374

220

Favorite

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        largest = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            if largest < cur:
                largest = cur
        return (largest)

