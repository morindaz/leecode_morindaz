# -*- coding: utf-8 -*-
# @Time    : 2019/9/10
# @Author  : morindaz
# @FileName: 50. Pow(x, n).py
# @explanation: This file is for:

"""
Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n%2:
            return x * self.myPow(x , n-1)
        return self.myPow(x*x, n /2)



if __name__ == '__main__':
    solution = Solution().myPow2(2,-2)
    print(solution)