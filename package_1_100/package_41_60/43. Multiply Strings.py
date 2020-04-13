"""
Given two non-negative integers num1 and num2 represented as strings,

return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def change_value(self, str_value):
    pass


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        change_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        res = 0
        for num_2 in num2:
            tmp = 0
            for num_1 in num1:
                tmp = tmp * 10 + int(num_1) * int(num_2)
            res = res * 10 + tmp
        return str(res)


if __name__ == '__main__':
    solution = Solution().multiply("123","456")
    print(solution)
