class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = self.helper(num)
        return ' '.join(res) if res else 'Zero'
        
    def helper(self, num):
        Ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        Tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        Hundreds = ['Hundred', 'Thousand', 'Million', 'Billion']
        res = []
        if num == 0:
            res = []
        elif num < 20:
            res.append(Ones[num - 1])
        elif num < 10**2:
            res.append(Tens[num // 10 - 2])
            res += self.helper(num % 10)
        elif num < 10**3:
            res += self.helper(num // 10**2)
            res.append(Hundreds[0])
            res += self.helper(num % 10**2)
        elif num < 10**6:
            res += self.helper(num // 10**3)
            res.append(Hundreds[1])
            res += self.helper(num % 10**3)
        elif num < 10**9:
            res += self.helper(num // 10**6)
            res.append(Hundreds[2])
            res += self.helper(num % 10**6)
        else:
            res += self.helper(num // 10**9)
            res.append(Hundreds[3])
            res += self.helper(num % 10**9)
        return res
