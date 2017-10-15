#Constant space solution.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m, n = len(matrix), len(matrix[0])
            rowHasZero, colHasZero = False, False
            if matrix[0][0] == 0:
                rowHasZero, colHasZero = True, True
            else:
                for i in range(1, m):
                    if matrix[i][0] == 0:
                        rowHasZero = True
                        break
                for j in range(1, n):
                    if matrix[0][j] == 0:
                        colHasZero = True
                        break
            if rowHasZero:
                for i in range(1, m):
                    matrix[i][0] = 1 if matrix[i][0] == 0 else 0
            if colHasZero:
                for j in range(1, n):
                    matrix[0][j] = 1 if matrix[0][j] == 0 else 0
            if rowHasZero or colHasZero:
                matrix[0][0] = 0
            for i in range(1, m):
                for j in range(1, n):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 1 if rowHasZero else 0
                        matrix[0][j] = 1 if colHasZero else 0
            for i in range(1, m):
                if matrix[i][0] == 1 and rowHasZero or matrix[i][0] == 0 and not rowHasZero:
                    for j in range(n):
                        matrix[i][j] = 0
            for j in range(1, n):
                if matrix[0][j] == 1 and colHasZero or matrix[0][j] == 0 and not colHasZero:
                    for i in range(m):
                        matrix[i][j] = 0
