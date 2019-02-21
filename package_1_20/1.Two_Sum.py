# -*- coding: utf-8 -*-
'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
-------------------
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            if ((target-nums[i]) in nums) and (nums.index(target-nums[i])!=i):
                result.append(i)
                result.append(nums.index(target-nums[i]))
                break
        return result

solution = Solution()
result = solution.twoSum([3,2,4],6)
print(result)

'''
解题思路：
1、target-nums[i]计算得到的数值在数组中
2、该数值的下标不与nums[i]的下标为同一个，为了避免将一个数字计算两遍的情况
'''