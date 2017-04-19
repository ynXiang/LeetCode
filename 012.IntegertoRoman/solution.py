class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['I', 'X', 'C' ,'M', 'V', 'L' ,'D']
        ans = ''
        i = 0
        while num > 0:
            tmp = num % 10
            if tmp <= 3:
                ans = tmp * roman[i] + ans
            elif tmp == 4:
                ans = roman[i] + roman[i+4] + ans
            elif tmp == 5:
                ans = roman[i+4] + ans
            elif tmp > 5 and tmp <= 8:
                ans = roman[i+4] + (tmp-5) * roman[i] + ans
            else:
                ans = roman[i] + roman[i+1] + ans
            num /= 10
            i += 1
        return ans