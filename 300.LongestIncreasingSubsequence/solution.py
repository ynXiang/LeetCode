#O(n^2) DP solution

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLen = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and maxLen[j] + 1 > maxLen[i]:
                    maxLen[i] = maxLen[j] + 1
        return max(maxLen)
