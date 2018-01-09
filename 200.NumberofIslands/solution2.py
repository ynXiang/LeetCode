class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def visit(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                grid[x][y] = '0'
                map(visit, (x-1, x+1, x, x), (y, y, y-1, y+1))
                return True
            return False
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visit(i, j):
                    cnt += 1
        return cnt
