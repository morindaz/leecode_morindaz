"""
1\
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Example
Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9

Example 2:
	Input:  [2,3,5,7], backpack size=12
	Output:  12

"""

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        if n< 0 or m < 0:
            return 0
        dp = [0 for _ in range(m + 1)]
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j-A[i]] + A[i], dp[j])
        return dp[-1]

if __name__ == '__main__':
    result = Solution().backPack(12, [2,3,5,7])
    print(result)