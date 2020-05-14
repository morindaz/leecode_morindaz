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
        self.list = []
        self._gen(0, 0, n, "")
        return self.list
    
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)

        if left < n:
            self._gen(left + 1, right, n, result + "(")
            print("left")
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")
            print("right")


class hanoi(object):
    def move(self,n, a, b, c):
        if n == 1:
            print(a, "->", c)
            return 0
        self.move(n-1, a, c, b)
        self.move(1, a, b, c)
        self.move(n-1, b, a, c)


if __name__ == '__main__':
    solution = Solution().generateParenthesis(3)
    print(solution)
    hanoi().move(3, "a", "b", "c")