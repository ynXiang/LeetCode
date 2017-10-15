class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = (b[::-1], a[::-1]) if len(a) > len(b) else (a[::-1], b[::-1])
        add, ans = 0, ""
        for i in range(len(a)):
            ans = str(int(a[i]) ^ int(b[i]) ^ add) + ans
            add = int((int(a[i]) + int(b[i]) + add) / 2)
        for v in b[len(a):]:
            ans = str(int(v) ^ add) + ans
            add = int((int(v) + add) / 2)
        return "1"+ans if add == 1 else ans
