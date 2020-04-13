"""
Given a string which consists of lowercase or uppercase letters,

find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_list = list(set(s))
        save_dict = {key : 0 for key in set_list}
        for tmp_s in s:
            save_dict[tmp_s] += 1
        result, flag = 0, 0
        for value in save_dict.values():
            if value % 2 != 0:
                flag = 1
            if value >= 2:
                result += int(value / 2) * 2
        if flag == 1:
            result += 1
        return result



if __name__ == "__main__":
    solution = Solution().longestPalindrome("abccccdd")
    print("success:", solution)