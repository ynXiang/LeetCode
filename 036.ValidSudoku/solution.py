class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for l in board:
            if len(set(l)-set(["."])) < 9 - l.count("."):
                return False
        for l in zip(*board):
            if len(set(l)-set(["."])) < 9 - l.count("."):
                return False
        for l3 in map(self.help,[board[:3], board[3:6], board[6:]]):
            for l in l3:
                if len(set(l)-set(["."])) < 9 - l.count("."):
                    return False
        return True
        
    def help(self, x):
        tmp = zip(*x)
        return [tmp[3*i]+tmp[3*i+1]+tmp[3*i+2] for i in range(3)]
