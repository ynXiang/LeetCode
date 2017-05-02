class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        absnum = abs(num)
        ans = ""
        while absnum > 0:
            ans = str(absnum%7) + ans
            absnum /= 7
        return ans if num > 0 else "-"+ans
