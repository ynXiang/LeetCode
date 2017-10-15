class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = n / 3
        b = n % 3
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif b == 0:
            return 3**a
        elif b == 1:
            return 3**(a-1)*4
        else:
            return 3**a*2
