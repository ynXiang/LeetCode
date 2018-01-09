#in-place

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        segOfPath = path.split('/')
        i, j = 0, 0
        while j < len(segOfPath):
            if segOfPath[j] not in ('', '.', '..'):
                segOfPath[i] = segOfPath[j]
                i += 1
            if segOfPath[j] == '..' and i > 0:
                i -= 1
            j += 1
        return '/' + '/'.join(segOfPath[:i])
