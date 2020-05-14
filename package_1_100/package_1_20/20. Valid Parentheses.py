"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parent_map = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char not in parent_map:
                stack.append(char)
            elif not stack or parent_map[char] != stack.pop():
                #not stack 为了保证如果栈为空时候没东西可以POP了
                return False
        return not stack


    def isValid2(self, s):
        stack = []
        bracket_dict = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char not in bracket_dict:
                stack.append(char)
            elif not stack or bracket_dict[char] != stack.pop(): #还有char的时候栈为空或者char与栈弹出的不一致
                return False
        return not stack #如果栈最后还有东西，说明不合法


if __name__ == '__main__':
    string = "]"
    solution = Solution()
    print(solution.isValid(string))