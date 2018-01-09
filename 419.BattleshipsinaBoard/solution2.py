class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.' or i > 0 and board[i-1][j] == 'X' or j > 0 and board[i][j-1] == 'X':
                    continue
                cnt += 1
        return cnt
