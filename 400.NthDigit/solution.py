class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        digits = 0
        while digits < n:
            digits += 9*10**(i-1)*i
            i += 1
        ans = (10**(i-1)-1) - int((digits-n)/(i-1))
        return int(str(ans)[i-2-(digits-n)%(i-1)])
