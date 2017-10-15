class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        cm, cn = click
        if board[cm][cn] == "M":
            board[cm][cn] == "X"
        else:
            pos = [click]
            while pos:
                m, n = pos[0]
                count = 0
                tmpPos = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if m+i >= 0 and m+i < len(board) and n+j >= 0 and n+j < len(board[0]):
                            if board[m][n] == "M":
                                count += 1
                            elif board[m][n] == "E":
                                tmpPos.append([m+i, n+j])
                board[m][n] == "B" if count == 0 else str(count)
                if count == 0:
                    pos += [p for p in tmpPos if p not in pos]
        return board
        
    def revealOnePos(self, board, click):
        m, n = click
        count = 0
        pos = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if m+i >= 0 and m+i < len(board) and n+j >= 0 and n+j < len(board[0]):
                    if board[m][n] == "M":
                        count += 1
                    pos.append([m+i, n+j])
        board[m][n] == "B" if count == 0 else str(count)
        return (board, pos) if count == 0 else (board, [])
                
        
