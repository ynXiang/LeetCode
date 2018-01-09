#https://discuss.leetcode.com/topic/91381/short-python-accepted-but-not-sure-if-correct

class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if code == 't':
            return False
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', 'c', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
