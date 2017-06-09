class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            if (1+i)*i/2 > n:
                return i-1
            i += 1
