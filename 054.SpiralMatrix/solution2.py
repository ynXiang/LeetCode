class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        return list(matrix[0]) + self.spiralOrder(zip(*matrix[1:])[::-1])
