#https://discuss.leetcode.com/topic/97631/two-java-dp-solution-o-n-2-and-o-n
#O(1) math solution is amazing!

class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 6: return N
        dp = [i+1 for i in xrange(N)]
        for i in xrange(6, N):
            dp[i] = max(dp[i-4]*3, dp[i-5]*4)
        return dp[-1]
