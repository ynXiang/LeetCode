class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 1
        m, n = len(dungeon), len(dungeon[0])
        health = [[1 for j in xrange(n)] for i in xrange(m)] # harm, minimum health
        health[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i == m-1 and j == n-1: continue
                if i == m-1: health[i][j] = max(health[i][j+1] - dungeon[i][j], 1)
                elif j == n-1: health[i][j] = max(health[i+1][j] - dungeon[i][j], 1)
                else: health[i][j] = max(min(health[i+1][j], health[i][j+1]) - dungeon[i][j], 1)
        return health[0][0]
