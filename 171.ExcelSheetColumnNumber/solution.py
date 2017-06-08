class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in s:
            ans = ans*26 + ord(i)-64
        return ans
