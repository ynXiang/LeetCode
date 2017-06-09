class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(2, numRows):
            ans.append([1])
            for j in range(i-1):
                ans[i].append(ans[i-1][j]+ans[i-1][j+1])
            ans[i].append(1)
        return ans
