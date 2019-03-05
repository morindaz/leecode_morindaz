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
        if left >= right:
            return arr
        flag = arr[left]
        while(left < right):
            while(arr[right] >= flag and left < right):
                right -= 1
            while(arr[left] <= flag and left < right):
                left += 1
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp

        # tmp = arr[left]
        arr[0] = arr[left]
        arr[left] = flag
        arr[left] = tmp
        self.quickSort(0,left-1, arr[:left])
        self.quickSort(left + 1,len(arr)-1, arr[left+1:])



    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sort = self.quickSort(0, len(nums)-1, nums)
        print("ss")

if __name__ == '__main__':
    solution = Solution().findKthLargest([3,2,3,1,2,4,5,5,6] ,4)
