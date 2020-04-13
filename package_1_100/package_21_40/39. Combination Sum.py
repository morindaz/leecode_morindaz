class Solution(object):
    def sum_all(self, remainder, stack, index):
        for i in range(index, len(self.candidates)):
            if remainder < self.candidates[i]:
                return
            elif remainder == self.candidates[i]:
                result = stack.copy()
                result.append(self.candidates[i])
                self.results.append(result)
                return
            else:
                stack.append(self.candidates[i])
                remainder = remainder - self.candidates[i]
                self.sum_all(remainder, stack, i)
                stack.pop()
                remainder += self.candidates[i]
        # return self.results


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        self.candidates = candidates
        self.candidates.sort()
        self.sum_all(target,[],0)
        return self.results


if __name__ == '__main__':
    solution = Solution().combinationSum([2,3,5], 8)
    print(solution)

