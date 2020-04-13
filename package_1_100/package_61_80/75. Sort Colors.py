"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,

 with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution(object):
    def quickSort(self, left, right, arr):
        tmp_left = left
        tmp_right = right
        if tmp_left >= tmp_right:
            return
        flag = arr[tmp_left]
        while(tmp_left < tmp_right):
            while(arr[tmp_right] >= flag and tmp_left < tmp_right):
                tmp_right -= 1
            while(arr[tmp_left] <= flag and tmp_left < tmp_right):
                tmp_left += 1
            tmp = arr[tmp_left]
            arr[tmp_left] = arr[tmp_right]
            arr[tmp_right] = tmp
        arr[left] = arr[tmp_left]
        arr[tmp_left] = flag
        self.quickSort(0,tmp_left-1, arr)
        self.quickSort(tmp_left + 1, right, arr)



    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # self.quickSort(0, len(nums)-1, nums)

        cnt = [0, 0, 0]
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        start = 0
        for index, times in enumerate(cnt):
            for time in range(times):
                nums[start] = index
                start += 1



if __name__ == '__main__':
    solution = Solution().sortColors( [2,0,2,1,1,0])
    print(solution)