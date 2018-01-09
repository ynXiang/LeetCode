class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def rotate(s, e, r, reverse):
            for k in range(r):
                if not reverse:
                    tmp = str[s]
                    for index in range(e-s):
                        str[s+index] = str[s+index+1]
                    str[e] = tmp
                else:
                    tmp = str[e]
                    for index in range(e-s):
                        str[s+index+1] = str[s+index]
                    str[s] = tmp
        i, j = 0, len(str) - 1
        while str[i] != ' ':
            i += 1
        if i == len(str):
            return
        while str[j] != ' ':
            j -= 1
        for k in range(min(i, len(str)-1-j)):
            str[k], str[j+1+k] = str[j+1+k], str[k]
        if i < j:
            rotate(0, j+i, i, False)
        elif i > j:
            rotate(len(str)-1-j, len(str)-1, len(str)-1-j, True)
        self.reverseWords(str[])
