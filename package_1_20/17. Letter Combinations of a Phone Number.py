# -*- coding: utf-8 -*-
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

from functools import reduce
class Solution(object):
    # 采用reduce的版本，哇啦哇啦说不能用
    # def reduce_comp(self, a, b):
    #     res = [ i+j for i in a for j in b] # 廖雪峰列表生成式全排列
    #     return res

    # 改成了自己的函数
    def reduce_self(self, list_a, list_b):
        res = [ i+j for i in list_a for j in list_b]
        return res



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        ref_dict = {
            "2" : ["a", "b", "c"],
            "3" : ["d","e","f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w","x", "y", "z"]
        }
        names = [ref_dict[key] for key in digits]
        # result = reduce(self.reduce_comp, names)
        result = names[0]
        for i in range(1, len(names)):
            result = self.reduce_self(result, names[i])
        print(result)
        return result



if __name__ == '__main__':
    solution = Solution()
    res = solution.letterCombinations("234")