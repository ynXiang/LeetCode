class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return False
        for i in range(1, int(len(s)/2+1)):
            if len(s) % i == 0:
                sub = True
                for j in range(len(s)/i):
                    if s[:i] != s[i*j:i*(j+1)]:
                        sub = False
                        break
                if sub:
                    return True
        return False
