class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        i, j = 1, num // 2
        k = (i+j) // 2
        while i <= j:
            if k**2 == num:
                return True
            elif k**2 > num:
                j = k - 1
            else:
                i = k + 1
            k = (i+j) // 2
        return False
