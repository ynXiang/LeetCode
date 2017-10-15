class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        return self.helper(matrix, 0, 0, len(matrix), len(matrix[0]), 0)
        
    def helper(self, matrix, startRow, startCol, numRows, numCols, direction):
        if numRows == 0 or numCols == 0:
            return []
        if direction == 0:
            return matrix[startRow][startCol:startCol+numCols] + self.helper(matrix, startRow+1, startCol, numRows-1, numCols, 1)
        elif direction == 1:
            return [matrix[row][startCol+numCols-1] for row in range(startRow, startRow+numRows)] + self.helper(matrix, startRow, startCol, numRows, numCols-1, 2)
        elif direction == 2:
            return matrix[startRow+numRows-1][startCol:startCol+numCols][::-1] + self.helper(matrix, startRow, startCol, numRows-1, numCols, 3)
        else:
            return [matrix[row][startCol] for row in range(startRow+numRows-1, startRow-1, -1)] + self.helper(matrix, startRow, startCol+1, numRows, numCols-1, 0)
