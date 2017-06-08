class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        add = 0
        ans = ""
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for i in range(0, len(num1)):
            s = ord(num1[i])-48 + ord(num2[i])-48 + add
            if s >= 10:
                add = 1
                s -= 10
            else:
                add = 0
            ans = chr(s+48) + ans
        for v in num2[len(num1):]:
            s = ord(v)-48 + add
            if s >= 10:
                add = 1
                s -= 10
            else:
                add = 0
            ans = chr(s+48) + ans
        if add == 1:
            ans = "1" + ans
        return ans
