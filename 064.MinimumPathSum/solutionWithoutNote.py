#If there is not restriction that you can only move either down or right at any point in time.

import heapq

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        waitingToVisit = []
        visited = [(0, 0)]
        heapq.heappush(waitingToVisit, (grid[0][0], 0, 0))
        while waitingToVisit:
            sumOfPath, x, y = heapq.heappop(waitingToVisit)
            if x > 0 and (x - 1, y) not in visited:
                visited.append((x - 1, y))
                heapq.heappush(waitingToVisit, (grid[x - 1][y] + sumOfPath, x - 1, y))
            if x < len(grid) - 1 and (x + 1, y) not in visited:
                if (x + 1, y) == (len(grid) - 1, len(grid[0]) - 1):
                    return grid[x + 1][y] + sumOfPath
                visited.append((x + 1, y))
                heapq.heappush(waitingToVisit, (grid[x + 1][y] + sumOfPath, x + 1, y))
            if y > 0 and (x, y - 1) not in visited:
                visited.append((x, y - 1))
                heapq.heappush(waitingToVisit, (grid[x][y - 1] + sumOfPath, x, y - 1))
            if y < len(grid[0]) - 1 and (x, y + 1) not in visited:
                if (x, y + 1) == (len(grid) - 1, len(grid[0]) - 1):
                    return grid[x][y + 1] + sumOfPath
                visited.append((x, y + 1))
                heapq.heappush(waitingToVisit, (grid[x][y + 1] + sumOfPath, x, y + 1))
