class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start, maxLen = 0, 1
        i = 0
        while i < len(s):
            j, k = i, i
            while k + 1 < len(s) and s[k] == s[k+1]:
                k += 1
            i = k + 1
            while j > 0 and k < len(s) - 1 and s[j-1] == s[k+1]:
                j -= 1
                k += 1
            if maxLen < k - j + 1:
                maxLen = k - j + 1
                start = j
        return s[start:start+maxLen]
