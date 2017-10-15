#https://discuss.leetcode.com/topic/22628/python-4-lines-short-solution-using-map

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([1])
            for j in range(i-1):
                ans[i].append(ans[i-1][j]+ans[i-1][j+1])
            ans[i].append(1)
        return ans
