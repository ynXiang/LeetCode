class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0:
                return a
            if b > a:
                return gcd(b, a)
            return gcd(b, a % b)
        return z == 0 or z <= x + y and z % gcd(x, y) == 0
