#https://discuss.leetcode.com/topic/85882/1-line-ruby-python

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for word in s.split(" "):
            ans += word[::-1] + " "
        return ans[:-1]
