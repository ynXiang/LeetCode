class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content = {}
        for l in paths:
            l = l.split()
            d, file = l[0], l[1:]
            for f in file:
                fn, fc = f[:-1].split("(")
                if fc not in content:
                    content[fc] = [d + "/" + fn]
                else:
                    content[fc].append(d + "/" + fn)
        return [g for g in content.values() if len(g) > 1]
