class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        x = abs(x)
        ans = 0
        while x > 0:
            ans += x % 10
            ans *= 10
            x = x / 10
        ans /= 10
        if ans >= 2**31:
            return 0
        else:
            if neg:
                return -ans
            else:
                return ans
