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
