class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        possiblePaths = [[0 for j in range(n)] for i in range(m)]
        possiblePaths[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m):
            possiblePaths[i][0] = possiblePaths[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            possiblePaths[0][j] = possiblePaths[0][j-1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            for j in range(1, n):
                possiblePaths[i][j] = possiblePaths[i-1][j] + possiblePaths[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return possiblePaths[m-1][n-1]
