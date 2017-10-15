class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[0 for q in range(n)] for p in range(m)]
                    if self.helper(board, word, i, j, visited):
                        return True
        return False
        
    def helper(self, board, word, x, y, visited):
        if not word:
            return True
        if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1 or visited[x][y] == 1 or board[x][y] != word[0]:
            return False
        visited[x][y] = 1
        if self.helper(board, word[1:], x-1, y, visited) or\
           self.helper(board, word[1:], x+1, y, visited) or\
           self.helper(board, word[1:], x, y-1, visited) or\
           self.helper(board, word[1:], x, y+1, visited):
            return True
        visited[x][y] = 0
        return False
