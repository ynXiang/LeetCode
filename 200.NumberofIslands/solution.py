class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def visit(x, y):
            if visited[x][y] or grid[x][y] == '0':
                return
            visited[x][y] = True
            if x > 0: visit(x-1, y)
            if x < len(grid)-1: visit(x+1, y)
            if y > 0: visit(x, y-1)
            if y < len(grid[0])-1: visit(x, y+1)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                visit(i, j)
                res += 1
        return resclass Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def visit(x, y):
            if visited[x][y] or grid[x][y] == '0':
                return
            visited[x][y] = True
            if x > 0: visit(x-1, y)
            if x < len(grid)-1: visit(x+1, y)
            if y > 0: visit(x, y-1)
            if y < len(grid[0])-1: visit(x, y+1)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                visit(i, j)
                res += 1
        return res
