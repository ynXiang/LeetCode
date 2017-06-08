class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        b = [0 for i in range(32)]
        change = ["a","b","c","d","e","f"]
        ans = ""
        neg = True if num < 0 else False
        num = abs(num)
        i = 31
        while num > 0:
            b[i] = num % 2
            num = int(num / 2)
            i -= 1
        if neg:
            add = 1
            for i in reversed(range(32)):
                b[i] ^= 1 ^ add
                if b[i] == 1:
                    add = 0
        for i in range(8):
            tmp = b[i*4]*8 + b[i*4+1]*4 + b[i*4+2]*2 + b[i*4+3]*1
            if tmp or ans:
                if tmp < 10:
                    ans += str(tmp)
                else:
                    ans += change[tmp-10]
        return ans
