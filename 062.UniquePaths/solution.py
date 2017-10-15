class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        possiblePaths = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                possiblePaths[i][j] = possiblePaths[i-1][j] + possiblePaths[i][j-1]
        return possiblePaths[m-1][n-1]
