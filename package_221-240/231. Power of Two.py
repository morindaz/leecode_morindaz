"""
Given an integer, write a function to determine if it is a power of two.
Example 1:
Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""


class Solution(object):
    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while(n % 2 == 0):
            n = n / 2
        if n == 1:
            return True
        else:
            return False

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 通过位运算的方式，非常的巧妙，如果是2^n的话那么只有一位是1
        if n == 0 :
            return False
        if n & n-1 == 0:
            return True
        else:
            return False

    # 大神的写法
    def isPowerOfTwo_m(self, n):
        return n > 0 and not (n & n-1)

if __name__ == '__main__':
    solution = Solution().isPowerOfTwo(4)
    print(solution)