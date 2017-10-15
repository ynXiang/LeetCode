#https://discuss.leetcode.com/topic/14626/1-liner-3-liner-4-liner

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.helper([i+1 for i in range(n)], k)
    
    def helper(self, nums, k):
        if k == 0:
            return [[]]
        res = []
        for i in range(len(nums)-k+1):
            res += [[nums[i]] + num for num in self.helper(nums[i+1:], k-1)]
        return res
