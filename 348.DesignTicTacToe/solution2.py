class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [[0, 0] for i in xrange(n)]
        self.cols = [[0, 0] for i in xrange(n)]
        self.diags = [[0, 0], [0, 0]]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        def update(status):
            if status[0] == 0:
                status[:] = [1, player]
            elif status[1] == player:
                status[0] += 1
            else:
                status[0] = -1
            return status[0] == self.n
        if update(self.rows[row]): return player
        if update(self.cols[col]): return player
        if row == col and update(self.diags[0]): return player
        if row + col == self.n - 1 and update(self.diags[1]): return player
        return 0
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
