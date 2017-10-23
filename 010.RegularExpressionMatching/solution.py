class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(char1, char2):
            return char1 == char2 or char1 == '.' or char2 == '.'
        dp = [[False for j in range (len(s)+1)] for i in range(len(p)+1)]
        dp[0][0] = True
        for i in range(2, len(s)+1):
            dp[0][i] = s[i-1] == '*' and dp[0][i-2]
        for i in range(2, len(p)+1):
            dp[i][0] = p[i-1] == '*' and dp[i-2][0]
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if match(p[i-1], s[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    if i == 1: return False
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i][j-1] and match(p[i-2], s[j-1]))
                elif s[j-1] == '*':
                    if j == 1: return False
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and match(p[i-1],s [j-2]))
        return dp[-1][-1]
