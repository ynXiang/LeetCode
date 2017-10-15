class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        sumOfPath = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    sumOfPath[i][j] = grid[i][j]
                else:
                    sumOfPath[i][j] = grid[i][j] + min(sumOfPath[i-1][j] if i > 0 else float('inf'), sumOfPath[i][j-1] if j > 0 else float('inf'))
        return sumOfPath[m-1][n-1]
