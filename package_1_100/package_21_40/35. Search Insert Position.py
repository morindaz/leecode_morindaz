"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if target < nums[0]:
                    return 0
                elif target > nums[-1]:
                    return len(nums)
                else:
                    if target > nums[i] and target<= nums[i+1]:
                        return i+1



if __name__ == '__main__':
    solution = Solution().searchInsert([1,3,5,5], 0)
    print(solution)