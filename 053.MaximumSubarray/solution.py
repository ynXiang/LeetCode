class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.count(nums)[0]
        
    def count(self, nums):
        if len(nums) == 1:
            return nums[0], nums[0]
        m, l = self.count(nums[:-1])
        l = l+nums[-1] if l > 0 else nums[-1]
        return max(m,l), l
