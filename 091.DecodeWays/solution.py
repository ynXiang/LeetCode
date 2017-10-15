class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        numOfWays = [0 for i in range(len(s))]
        numOfWays[0] = 0 if s[-1] <= '0' or s[-1] > '9' else 1
        for i in range(1, len(s)):
            if s[-i-1] == '1' and s[-i] >= '0' and s[-i] <= '9' or s[-i-1] == '2' and s[-i] >= '0' and s[-i] <= '6':
                numOfWays[i] = numOfWays[i-1] + (numOfWays[i-2] if i > 1 else 1)
            elif s[-i-1] <= '0' or s[-i-1] > '9':
                numOfWays[i] = 0
            else:
                numOfWays[i] = numOfWays[i-1]
        print numOfWays
        return numOfWays[-1]
