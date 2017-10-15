#https://discuss.leetcode.com/topic/12587/my-solution-in-c-o-1-space-and-no-magic-math-property-involved

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
