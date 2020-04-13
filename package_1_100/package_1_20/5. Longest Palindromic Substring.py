# -*- coding: utf-8 -*-
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        head = 0
        tail = 0
        max_str = ""
        while head  <= len(s):
            while tail <= len(s):

                tmp_str = s[head: tail]
                if tmp_str == tmp_str[::-1] and len(tmp_str) > len(max_str):
                    max_str = tmp_str
                    tail += 1

            head += 1
            tail = head + 1
            return max_str



    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        head = 0
        tail = 0
        max_len = 0
        max_str =""
        while(head<=tail and head<len(s)):
            while(tail<=len(s)):
                hash = s[head:tail]
                if(hash==hash[::-1] and (len(hash)>=max_len)):
                    max_len= len(hash)
                    max_str = hash
                tail += 1
            head+=1
            tail = head+1
        return max_str
solution = Solution()
result = solution.longestPalindrome("cbbc")
print(result)

'''
解题思路：
这里利用了python的一个黑科技hash==hash[::-1] 直接用来判断字符串是不是回文
接着用一个类似于滑窗的思路，和之前的第3题解题思路非常相似
首先固定头指针不动，移动尾指针，并且头尾之间的为hash表 用来判断是不是回文
尾指针到最后时，移动头指针，令尾指针等于头指针之后的那个字符
循环到数组结束
'''