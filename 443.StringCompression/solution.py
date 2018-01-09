class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(chars):
            cnt = 1
            chars[i] = chars[j]
            i += 1
            while j < len(chars)-1 and chars[j+1] == chars[j]:
                j += 1
                cnt += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[i] = c
                    i += 1
            j += 1
        return i
