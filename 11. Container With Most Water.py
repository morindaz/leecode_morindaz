# -*- coding: utf-8 -*-

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        head = 0
        tail = len(height)-1
        while(head<=tail):
            while(tail>head and tail>0):
                volume = min(height[head],height[tail])*(tail-head)
                if volume>max:
                    max = volume
                tail-=1
            head+=1
            tail=len(height)-1
        return max

solutoin = Solution()
result = solutoin.maxArea([2,3,4,5,18,17,6])
print(result)

'''
这里主要遇到了超时问题
'''
