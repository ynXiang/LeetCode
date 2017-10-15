#https://discuss.leetcode.com/topic/23607/1-liner-in-ruby-python

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
        k = int((i+j)/2)
        while i != k or k != j:
            if isBadVersion(k):
                j = k
            else:
                i = k + 1
            k = int((i+j)/2)
        return k
