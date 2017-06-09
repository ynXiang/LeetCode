class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.comb(i, rowIndex))
        return ans
        
    def comb(self, m, n):
        ans = 1
        for i in range(n-m+1, n+1):
            ans *= i
        for i in range(1, m+1):
            ans /= i
        return ans
