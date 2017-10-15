class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = a.split("+")
        a1, a2 = int(a1), int(a2[:-1])
        b1, b2 = b.split("+")
        b1, b2 = int(b1), int(b2[:-1])
        c1 = a1 * b1 - a2 * b2
        c2 = a1 * b2 + a2 * b1
        return str(c1) + "+" + str(c2) + "i"
