class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sig = s[0]
        count = 0
        counts = []
        for char in s:
            if char == sig:
                count += 1
            else:
                counts.append(count)
                count = 1
                sig = char
        counts.append(count)
        return reduce(lambda x, y: x + y, map(lambda x, y: min(x, y), counts[:-1], counts[1:]), 0)
