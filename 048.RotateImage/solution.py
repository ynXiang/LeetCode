class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for row in range((l + 1) // 2):
            for col in range(l // 2):
                matrix[row][col], matrix[col][l-1-row], matrix[l-1-row][l-1-col], matrix[l-1-col][row] = matrix[l-1-col][row], matrix[row][col], matrix[col][l-1-row], matrix[l-1-row][l-1-col]
