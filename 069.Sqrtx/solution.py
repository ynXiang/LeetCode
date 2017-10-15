class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        i = 1
        j = x
        while int((i+j)/2)**2 > x or int((i+j)/2+1)**2 <= x:
            if int((i+j)**2/4) < x:
                i = int((i+j)/2) + 1
            else:
                j = int((i+j)/2) - 1
        return int((i+j)/2)
