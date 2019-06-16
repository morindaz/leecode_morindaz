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
    def threeSum2(self, nums):
        """
        用map或者set的方式
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i,v in enumerate(nums[:-2]):
            if i >=1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))



    def threeSum(self, nums):
        """
        思路是两重循环
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
        """
        先排序，然后用三个指针
        :param nums:
        :return:
        """
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
                    if tmp < 0:
                        left += 1
                    if tmp > 0:
                        right -= 1
        final = []
        for res in result:
            if res not in final:
                final.append(res)
        return final

    def threeSum2(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) -1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0 : l += 1
                elif s > 0 : r -= 1
                else:
                    res.append((nums[i], nums[l] ,nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return list(map(list, res))



if __name__ == '__main__':
    # a = [2,3,4,5,2]
    # print(a.index(5))
    solution = Solution()
    # result = solution.threeSum2([1,2,-3])
    result = solution.threeSum2([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])
    print(result)


'''
[0,0,0]   
https://www.hrwhisper.me/leetcode-2-sum-3-sum-4-sum-3-sum-closest-k-sum/
'''