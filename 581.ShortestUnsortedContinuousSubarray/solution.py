#https://discuss.leetcode.com/topic/89282/java-o-n-time-o-1-space

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sortnums = sorted(nums)
        i = 0
        while i < len(nums) and sortnums[i] == nums[i]:
            i += 1
        if i == len(nums):
            return 0
        j = len(nums)-1
        while sortnums[j] == nums[j]:
            j -= 1
        return j-i+1
