class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ans = [matrix[0][0]]
        i = j = 0
        m, n = len(matrix), len(matrix[0])
        while i != m-1 or j != n-1:
            if (i + j) % 2 == 0:
                if j == n-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i, j = i-1, j+1
            else:
                if i == m-1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i, j = i+1, j-1
            ans.append(matrix[i][j])
        return ans
