class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        ans = 0
        hasodd = False
        for i in dict.values():
            if i % 2 == 0:
                ans += i
            else:
                if hasodd:
                    ans += i - 1
                else:
                    ans += i
                    hasodd = True
        return ans
