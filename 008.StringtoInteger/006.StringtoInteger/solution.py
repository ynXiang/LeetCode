class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        intstr = '0123456789'
        if str == '':
            return 0
        elif len(str) == 1:
            if str in intstr:
                return int(str)
            else:
                return 0
        indent = 0
        while str[indent] == ' ':
            indent += 1
        neg = str[indent] == '-'
        indent += neg or str[indent] == '+'
        ans = 0
        for _ in str[indent:]:
            if _ in intstr:
               ans = ans * 10 + int(_)
            else:
                break
        ans = (1 - neg * 2) * ans
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN
        else:
            return ans
