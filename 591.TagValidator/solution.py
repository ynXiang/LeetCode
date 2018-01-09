class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        import re
        if len(code) < 2 or code[0] != '<' or code[1] == '!':
            return False
        stack = []
        i, l = 0, len(code)
        while i < l:
            if code[i] == '<':
                closed = i < l - 1 and code[i+1] == '/'
                cdata = i < l - 8 and code[i+1:i+9] == '![CDATA['
                j = i + 1
                while j < l:
                    if cdata and code[j-2:j+1] != ']]>' or not cdata and code[j] != '>': j += 1
                    else: break
                if j == l: return False
                if closed:
                    if not stack or code[i+2:j] != stack.pop() or (j != l - 1 and not stack): return False
                elif not cdata:
                    if j == i + 1 or j > i + 10 or re.search(r'[^A-Z]', code[i+1:j]): return False
                    else: stack.append(code[i+1:j])
                i = j
            i += 1
        return not stack
