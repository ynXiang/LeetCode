class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                res = -board[i][j]
                for p in xrange(max(0, i-1), min(m, i+2)):
                    for q in xrange(max(0, j-1), min(n, j+2)):
                        res += board[p][q] % 2
                if res == 2 and board[i][j] == 1 or res == 3:
                    board[i][j] += 2
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = 1 if board[i][j] >= 2 else 0
