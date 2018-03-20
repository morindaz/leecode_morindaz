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
            volume = min(height[head],height[tail])*(tail-head)
            if volume>max:
                max = volume
            if height[tail]>height[head]:
                head+=1
            else:
                tail-=1
        return max

solutoin = Solution()
result = solutoin.maxArea([2,3,4,5,18,17,6])
print(result)

'''
这里主要遇到了超时问题,如果选用两层循环的话，会超时
设置两层循环的方法为：左边head，右边tail
第一种方式最蠢，头尾指针同一个方向移动。也就是尾指针在头指针后面，头指针走一格，尾指针从头指针后一直走到最后。
然后采用高乘以宽的方式来计算结果。尾巴指针一直往后，设置一个max存放最大的容量。
第二种方式稍微改进了一点，头指针指最前，尾指针指最后，当头尾指针相遇的时候就停止。这样也需要一直循环，因为头指针向前走一格，尾指针每次都要从最后一直向中间走
直到碰到头指针为止。
第三种方式也就是能够accept的方法，则比较聪明。
从两端开始，哪边高，那么另外一边移动，直到两个指针碰到为止
'''
