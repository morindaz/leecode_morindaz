# -*- coding: utf-8 -*-
'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if(x<0):
        #     x = x*(-1)
        if x<(-2147483648) or x>2147483647:
            return False
        x = str(x)

        if(x==x[::-1]):
            result = int(x[::-1])
            if result>=(-2147483648) or result<=2147483647:
                return True
        return False

solution  =Solution()
result = solution.isPalindrome(-2147447412)
print(result)

'''
解题思路：
在python里面判断回文其实非常简单，x==x[::-1] 这是个非常作弊的手法
这题判断一下有没有越界，负数的话不算回文。其余的话很简单啦，将数字转换成字符
不把数字转换成字符好像没有办法做循环，在c++里面就比较麻烦，还需要将数字一个个取出来。
cpp需要将数字变成一个数组，通过%的方式取出一个个数字吗？不太确定。

'''