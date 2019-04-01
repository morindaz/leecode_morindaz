"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = list(set(nums))
        num_dict = {key : 0 for key in num_set}
        for num in nums:
            num_dict[num] += 1
        result = sorted(num_dict.items(), key = lambda x:x[1],reverse=True)[0][0]
        return result


if __name__ == '__main__':
    solution = Solution().majorityElement([2,2,1,1,1,2,2,3])
    print(solution)