# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        ans = int((l+r)/2)
        while True:
            t = guess(ans)
            if t == -1:
                r = ans - 1
                ans = int((l+r)/2)
            elif t == 1:
                l = ans + 1
                ans = int((l+r)/2)
            else:
                return ans
