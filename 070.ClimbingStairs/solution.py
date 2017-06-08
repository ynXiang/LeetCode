'''Fibonacci'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        numOf2 = int(n/2)
        ans = 0
        for i in range(numOf2+1):
            ans += self.comb(i, n-i*2)
        return ans
    
    def comb(self, m, n):
        if m > n:
            m, n = n, m
        ans = 1
        for i in range(m):
            ans *= (m+n-i)
        for i in range(m):
            ans /= (i+1)
        print m,n,ans
        return ans
