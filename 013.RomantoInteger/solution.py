class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = [1, 5, 10, 50 ,100, 500, 1000]
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        pre = 0
        ans = 0
        for _ in s:
            cur = num[roman.index(_)]
            if pre < cur:
                ans += cur - 2 * pre
            else:
                ans += cur
            pre = cur
        return ans