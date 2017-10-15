class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                    m, n = i-1, j
                    while m >= 0 and board[m][n] == 'X':
                        board[m][n] = '.'
                        m -= 1
                    m, n = i+1, j
                    while m < len(board) and board[m][n] == 'X':
                        board[m][n] = '.'
                        m += 1
                    m, n = i, j-1
                    while n >= 0 and board[m][n] == 'X':
                        board[m][n] = '.'
                        n -= 1
                    m, n = i, j+1
                    while n < len(board[0]) and board[m][n] == 'X':
                        board[m][n] = '.'
                        n += 1
        return count
