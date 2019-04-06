"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution(object):
    # 动态规划的方法 但是也比较慢
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [1 for i in range(n+1)]
        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]
        return F[n]

    #斐波那契数列 超时了
    def climbStairs(self, n):
        if n <= 1:
            return 1
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairs_su(self, n):
        x , y = 1 ,1
        for _ in range(1, n):
            x, y = y, x + y
        return y


if __name__ == "__main__":
    solution = Solution().climbStairs_su(2)
    print(solution)
    print("success")

"""
经典爬楼梯动态规划采用类似于裴伯纳斯的思维，可以通过递推的方法
"""