import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = re.sub(r'[^a-z0-9]','',s.lower())
        return s1 == s1[::-1]
