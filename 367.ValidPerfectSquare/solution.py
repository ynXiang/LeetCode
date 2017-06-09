class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while True:
            if i**2 == num:
                return True
            elif i**2 > num:
                return False
            i += 1
