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


class Solution2(object):
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


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            if i >= 1 and nums[i] == nums[i-1]:
                pass
            else:
                while left < right:
                    tmp = nums[i] + nums[left] + nums[right]
                    if tmp == 0 :
                        result.append([nums[i], nums[left] , nums[right]])
                        left += 1
                        right -= 1
                        # while nums[left] == nums[left-1]:
                        #     left += 1
                        # while nums[right] == nums[right+1]:
                        #     right -= 1

                    if tmp < 0:
                        left += 1
                    if tmp > 0:
                        right -= 1
        final = []
        for res in result:
            if res not in final:
                final.append(res)

        return final



if __name__ == '__main__':
    # a = [2,3,4,5,2]
    # print(a.index(5))
    solution = Solution()
    result = solution.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])
    print(result)


'''
[0,0,0]   
https://www.hrwhisper.me/leetcode-2-sum-3-sum-4-sum-3-sum-closest-k-sum/
'''