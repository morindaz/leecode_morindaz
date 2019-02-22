# -*- coding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]

        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                re = []
                sum_ne  = -(nums[i] + nums[j])
                if sum_ne in (nums[j+1:]):
                    re.append(nums[i])
                    re.append(nums[j])
                    re.append(sum_ne)
                else:
                        pass
                if re != []:
                    re.sort()
                    if re in result:
                        pass
                    else:
                        result.append(re)
        return result


if __name__ == '__main__':
    # a = [2,3,4,5,2]
    # print(a.index(5))
    solution = Solution()
    result = solution.threeSum([-1,0,1,2,-1,-4])
    print(result)


'''
[0,0,0]   
https://www.hrwhisper.me/leetcode-2-sum-3-sum-4-sum-3-sum-closest-k-sum/
'''