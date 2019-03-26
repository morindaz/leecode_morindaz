"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        flag =  "-" if num < 0 else ""
        num = abs(num)
        result = ''
        while(num > 0):
            result = str(num % 7) + result
            num = int(num / 7)
        result = flag + result
        return result

if __name__ == "__main__":
    solution = Solution().convertToBase7(-7)
    print(solution)