# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        head =tail = 0
        while(tail<len(s)):

            hash = s[head:(tail)]
            if(s[tail] in hash):
                head = head+1
                len2 = tail-head+1
                max_len = max(max_len,len2)
            else:
                # print(s[head:tail])
                length = tail-head+1
                max_len= max(max_len,length)
                # print(max_len)
                tail += 1
        return max_len

solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)


'''
解题思路：
1、采用两个指针，头指针和尾指针，尾指针先移动。头指针和尾指针之间的长度为比对字符串。
2、如果尾指针所指的字符不在比对字符串中，则长度增加1，尾指针向后移动，得到最长长度
3、如果尾指针所指的字符在比对字符串中，则头指针向后移动，得到最长长度

'''