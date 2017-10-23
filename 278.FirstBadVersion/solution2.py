# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        k = (i+j) // 2
        while i < j:
            if isBadVersion(k):
                j = k
            else:
                i = k + 1
            k = (i + j) // 2
        return k if isBadVersion(k) else k + 1
