class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(len(nums))] for j in range(2)]
        for i in range(len(nums)):
            if i == 0:
                dp[0][i] = nums[0]
            else:
                for k in range(2):
                    dp[k][i] = max(i > 0 and dp[k][i-1], (i > 1 and dp[k][i-2]) + nums[i])
        return max(dp[0][-2], dp[1][-1]) if len(nums) > 1 else nums[0] if len(nums) == 1 else 0
