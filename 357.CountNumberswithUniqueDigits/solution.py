class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [1]
        ans = [1]
        for i in range(min(n, 9)):
            count.append(count[-1] * (10-i))
            ans.append(count[-1] * 9/10 + ans[-1])
        return ans[-1]
