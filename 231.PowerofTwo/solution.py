class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        while n % 2 == 0:
            n /= 2
            if n == 1:
                return True
        return False
