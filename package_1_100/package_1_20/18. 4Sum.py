"""
Given an array nums of n integers and an integer target, are there elements a, b, c,
 and d in nums such that a + b + c + d = target?
 Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution(object):
    def threeSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i >= 1 and nums[i] == nums[i - 1]:
                pass
            else:
                while left < right:
                    tmp = nums[i] + nums[left] + nums[right]
                    if tmp == target:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    if tmp < target:
                        left += 1
                    if tmp > target:
                        right -= 1
        final = []
        for res in result:
            if res not in final:
                final.append(res)
        return final

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            new_target = target - nums[i]
            tmp = self.threeSum(nums[i+1:], new_target)
            if tmp != []:
                for j in tmp:
                    j.append(nums[i])
                    print("insert", nums[i])
                    j.sort()
                result.extend(tmp)
        final = []
        for res in result:
            if res not in final:
                final.append(res)
        return final


if __name__ == '__main__':
    solution = Solution().fourSum([5,5,3,5,1,-5,1,-2], 4)
    print(solution)

"""
就是在3sum基础上做的改进
"""