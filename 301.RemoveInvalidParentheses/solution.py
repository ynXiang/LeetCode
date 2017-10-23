class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for char in s:
                if char == '(':
                    cnt += 1
                elif char == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        strings = set([s])
        while True:
            validStrs = []
            for string in strings:
                if isValid(string):
                    validStrs.append(string)
            if validStrs:
                return validStrs
            strings = set([string[:i]+string[i+1:] for i in range(len(string)) for string in strings]) 
