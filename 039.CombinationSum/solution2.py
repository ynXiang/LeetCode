#dp
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not candidates[0]:
            return []
        dp = [[[] for j in xrange(target+1)] for i in xrange(len(candidates))]
        for i in xrange(len(candidates)):
            for j in xrange(target+1):
                if j == 0:
                    dp[i][j].append([])
                    continue
                if i > 0: dp[i][j] += dp[i-1][j]
                if j >= candidates[i]: dp[i][j] += [pre + [candidates[i]] for pre in dp[i][j-candidates[i]]]
        return dp[-1][-1]
