class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.numStones = [0 for i in range(n*2+2)] # row, col, main diag, sub diag
        self.status = [0 for i in range(n*2+2)]
        

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
        def helper(k):
            if k == -2 and row != col or k == -1 and row + col != self.n - 1:
                return 0
            if self.status[k] == player or self.status[k] == 0:
                self.status[k] = player
                self.numStones[k] += 1
                if self.numStones[k] == self.n:
                    return player
            else:
                self.status[k] = -1
            return 0
        return helper(row) or helper(col + self.n) or helper(-2) or helper(-1)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
