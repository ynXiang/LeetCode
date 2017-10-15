class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix)
        m = (i + j) // 2
        while i < j:
            if target < matrix[m][0]:
                j = m
            elif target > matrix[m][0]:
                i = m + 1
            else:
                return True
            m = (i + j) // 2
        m -= 1    
        i, j = 0, len(matrix[0])
        n = (i + j) // 2
        while i < j:
            if target < matrix[m][n]:
                j = n
            elif target > matrix[m][n]:
                i = n + 1
            else:
                return True
            n = (i + j) // 2
        return False
