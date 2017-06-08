class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        i = 0
        while 2*i*k < len(s):
            ans += s[2*i*k:(2*i+1)*k][::-1]
            ans += s[(2*i+1)*k:(2*i+2)*k]
            i += 1
        return ans
