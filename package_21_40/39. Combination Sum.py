class Solution:

    def combinationSum(self, candidates, target: int):
        self.results = []
        self.candidates = candidates
        self.candidates.sort()

        self.dfs(target, [], 0)

        return self.results

    def dfs(self, remainder, stack, index):

        for i in range(index, len(self.candidates)):

            candidate = self.candidates[i]

            if remainder < candidate:
                return

            if remainder == candidate:
                result = stack.copy()
                result.append(candidate)
                self.results.append(result)
                return

            remainder -= candidate
            stack.append(candidate)

            self.dfs(remainder, stack, i)

            stack.pop()
            remainder += candidate


if __name__ == '__main__':
    solution = Solution()
    # print((solution.combinationSum([3, 2, 6, 7, 8, 9], 7)))
    print((solution.combinationSum([2,3,5], 8)))
