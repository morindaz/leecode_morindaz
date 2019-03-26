"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        for i in range(n):
            result = self.get_next_sequence(result)
        return result

    def get_next_sequence(self, previous_sequence):
        left = 0
        next_sequence = ''
        if len(previous_sequence) == 0:
            return '1'
        for right in range(len(previous_sequence)):
            if right == len(previous_sequence) - 1 or previous_sequence[right] != previous_sequence[right+1]:
                next_sequence = self.say(previous_sequence[left: right+1], next_sequence)
                left = right + 1
        return next_sequence


    def say(self, sequence, result):
        tmp = str(len(sequence)) + sequence[0]
        result += tmp
        return result

if __name__ == '__main__':
    solution = Solution().countAndSay(4)
    print(solution)

