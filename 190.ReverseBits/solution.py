#https://discuss.leetcode.com/topic/10069/python-ac-with-63ms-3lines
#https://discuss.leetcode.com/topic/9811/o-1-bit-operation-c-solution-8ms/2

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            if n != 0:
                ans = (ans + n % 2) * 2
                n = int(n / 2)
            else:
                ans *= 2
        return ans/2
