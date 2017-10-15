class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        return self.myPow(x**2, n//2) if n % 2 == 0 else self.myPow(x**2, n//2) * x
