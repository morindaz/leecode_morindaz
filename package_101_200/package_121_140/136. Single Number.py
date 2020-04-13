"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    #reference1
    def singleNumber1(self, nums):
        return 2 * sum(set(nums))-sum(nums)

    #mysolution
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result  = result ^ num
        return result


if __name__ == '__main__':
    solution = Solution().singleNumber1([2,2,10])
    print(solution)


# notation
"""
这里的元素只出现两次或者一次，但是如果可以出现四次的话这个方法就不适用了
"""