# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        prefix = strs[0]
        for i in strs:
            length = min(len(prefix),len(i))
            prefix = prefix[0:length]
            for j in range(length):
                if prefix[j]!=i[j] :
                    prefix = i[0:j]
                    break
                else:
                    pass

        return prefix

solution = Solution()
result = solution.longestCommonPrefix(["aa","a"])
print(result)
'''
这题需要注意的是需要将prefix进行截断操作，否则的话出现"aa","a"的情况，那么prefix就会选择前面较长的的字符串
只要设置一个目标 然后一个一个比较就行了
本来还想有一种操作就是同时取出数组中每个字符串的第一个字母
'''