class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        segOfPath = path.split('/')
        numOfBack = segOfPath.count('..')
        res = []
        for path in segOfPath:
            if path not in ['', '.', '..']:
                res.append(path)
            elif path == '..' and res:
                del res[-1]
        return '/' + '/'.join(res)
