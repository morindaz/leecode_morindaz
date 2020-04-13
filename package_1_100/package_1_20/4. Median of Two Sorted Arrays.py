# -*- coding: utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 or not nums2:
            return 0



    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1)
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        length = len(nums1)
        if(length%2==0):
            index = int((length/2)-1)
            a1 = nums1[index]
            a2 = nums1[int(length/2)]
            result = (a1+a2)/2
        else:
            result = nums1[int(math.floor(length/2))]
        return result

a= [2,3,4]
print(a[0])
solution = Solution()
result = solution.findMedianSortedArrays([1,2],[3,4])
print (result)

'''
解题思路：
这题要求是run time complexity should be O(log (m+n))
这边采用了将两个数组拼接 num1.extend方法
之后将数组排序num1.sort()方法
最后通过数组里面包含的数量是基数还是偶数来进行判断
但是python的extend方法和sort方法的时间复杂度是多少感觉不是很清楚- -
'''