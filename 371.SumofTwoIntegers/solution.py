class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        re = False
        if a == -b:
            return 0
        elif (a > 0 and b < 0 and a > -b) or (a < 0 and b > 0 and -a < b):
            a = -a
            b = -b
            re = True
        while a != 0:
            tmp = (a & b) << 1
            b ^= a
            a = tmp
        return -b if re else b
