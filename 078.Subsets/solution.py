class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for k in range(len(nums)+1):
            res += self.helper(nums, k)
        return res
    
    def helper(self, nums, k):
        if k == 0:
            return [[]]
        return [pre + [nums[i]] for i in range(len(nums)) for pre in self.helper(nums[:i], k-1)]
