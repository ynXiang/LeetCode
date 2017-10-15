#https://discuss.leetcode.com/topic/30140/use-n-n-n-1-trick-to-clear-the-least-bit/4

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n % 2
            n = int(n / 2)
        return count
