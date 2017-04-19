class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parent = list()
        for _ in s:
            if _ == '(' or _ == '[' or _ == '{':
                parent.append(_)
            elif _ == ')' and (len(parent) == 0 or parent.pop() != '('):
                return False
            elif _ == ']' and (len(parent) == 0 or parent.pop() != '['):
                return False
            elif _ == '}' and (len(parent) == 0 or parent.pop() != '{'):
                return False
        if len(parent) == 0:
            return True
        else:
            return False
