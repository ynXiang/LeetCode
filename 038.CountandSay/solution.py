#https://discuss.leetcode.com/topic/32023/4-5-lines-python-solutions

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in range(n-1):
            ans = self.update(ans)
        return ans

    def update(self, s):
        count = 1
        c = s[0]
        ans = ""
        for i in s[1:]:
            if i == c:
                count += 1
            else:
                ans += str(count) + c
                count = 1
                c = i
        ans += str(count) + c
        return ans
