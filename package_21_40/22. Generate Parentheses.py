"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list =  []
        self._gen(0, 0, n, "")
        return self.list
    
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)

        if left < n:
            self._gen(left + 1, right, n, result + "(")
        if left >  right and right < n:
            self._gen(left, right + 1, n, result + ")" )

solution = Solution().generateParenthesis(5)
print(solution)


if __name__ == '__main__':
    solution = Solution().generateParenthesis(3)
    print(solution)