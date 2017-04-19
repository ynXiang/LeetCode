class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        scale = numRows * 2 - 2
        count = len(s) / scale + 1
        ans = list()
        for j in range(scale/2+1):
            for i in range(count):
                if j != 0 and j != scale / 2 and (i+1) * scale - j < len(s):
                    ans.append(s[i * scale + j] + s[(i+1) * scale - j])
                else:
                    if i * scale + j >= len(s):
                        break
                    ans.append(s[i * scale + j])
        return ''.join(ans)
