class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for char in s:
            ans ^= ord(char)
        for char in t:
            ans ^= ord(char)
        return chr(ans)
