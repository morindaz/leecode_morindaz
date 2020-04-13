"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if len()
        tmp_list = {i:0 for i in nums}

        for num in nums:
            tmp_list[num] += 1
        # save = tmp_list.copy()
        save = sorted(tmp_list.items(), key= lambda x:x[1], reverse=True)
        result = list()
        for i in range(k):
            result.append(save[i][0])
        return result





if __name__ == '__main__':
    solution = Solution().topKFrequent([1,1,1,2,2,3], 2)
    print(solution)