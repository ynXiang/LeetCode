class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 4:
            return False
        ans = 0
        while n > 0:
            ans += (n % 10)**2
            n = int(n / 10)
        return self.isHappy(ans)
