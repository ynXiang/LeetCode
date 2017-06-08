class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        if m+1 == len(nums):
            return m+1
        ans = 0
        for i in range(m+1):
            ans ^= i
        for i in nums:
            ans ^= i
        return ans
