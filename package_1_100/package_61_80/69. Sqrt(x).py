"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 1
        right = x/2
        last_mid = 0

        while(left <= right):
            mid = int((right+left) / 2)
            if (mid < x / mid):
                left = mid + 1
                last_mid = mid
            elif(mid > x / mid):
                right = mid - 1
            else:
                return mid

        return int(last_mid)


if __name__ == '__main__':
    solution = Solution().mySqrt(4)
    print(solution)

"""
这道题目就是疯狂考验边界条件加上二分法则
"""