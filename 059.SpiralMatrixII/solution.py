#https://discuss.leetcode.com/topic/19130/4-9-lines-python-solutions

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        i, cur = 2, n*n
        while i/2.0 <= n:
            res = [[cur-i//2+k+1 for k in range(i//2)]] + zip(*res[::-1])
            cur -= i//2
            i += 1
        return res
