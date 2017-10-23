class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        res = []
        if num[0] == '0':
            self.helper(num[1:], res, '0', 0, target, 0, '')
        else:
            for i in range(len(num)):
                self.helper(num[i+1:], res, num[:i+1], int(num[:i+1]), target, int(num[:i+1]), '')
        return res
        
    def helper(self, num, res, expr, totalValue, target, preValue, preOp):
        if totalValue == target and not num:
            res.append(expr)
            return
        for i in range(len(num)):
            curStr = num[:i+1]
            curValue = int(curStr)
            self.helper(num[i+1:], res, expr+'+'+curStr, totalValue+curValue, target, curValue, '+')
            self.helper(num[i+1:], res, expr+'-'+curStr, totalValue-curValue, target, curValue, '-')
            if preOp == '+':
                tmpValue = totalValue - preValue + preValue * curValue
            elif preOp == '-':
                tmpValue = totalValue + preValue - preValue * curValue
            else:
                tmpValue = totalValue * curValue
            self.helper(num[i+1:], res, expr+'*'+curStr, tmpValue, target, preValue*curValue, preOp)
            if num[0] == '0':
                break
