# -*- coding: utf-8 -*-

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < 0):
            flag = -1
        else:
            flag = 1
        x = x * flag
        result = 0
        while(x>0):
            result =result*10+int(x%10)
            x = int(x/10)
        result*=flag
        if x<(-2147483648) or x>2147483647 or result<-2147483648 or result>2147483648:
            return 0
        return result


solution = Solution()
result = solution.reverse(1534236469)
print(result)

'''
解题思路：
好吧非常简单的题目，但是需要做溢出检查，不但是输入的数据要在条件内，输出的数据也要在条件内。
'''