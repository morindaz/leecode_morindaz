"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
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



    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # self.quickSort(0, len(nums)-1, nums)
        nums.sort()
        print(nums)
        return nums[-k]

if __name__ == '__main__':
    solution = Solution().findKthLargest( [3,2,3,1,2,4,5,5,6] ,4)
    print(solution)
