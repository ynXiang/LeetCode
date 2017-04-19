class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if s[0] == s[1]:
            cur_len = 2
            max_len = 2
            max_index = 2
            pali_end = True
            same = True
        else:
            cur_len = 1
            max_len = 1
            max_index = 1
            pali_end = False
            same = False
        i = 2
        while i < len(s):
            if pali_end:
				if same and s[i] == s[i-1]:
					cur_len += 1
				else:
					same = False
					if i - cur_len <= 0 or s[i] != s[i-cur_len-1]:
						pali_end = False
						if max_len < cur_len:
							max_len = cur_len
							max_index = i
						if cur_len > 3:
						    i -= int(cur_len/2 - 1)
					else:
						cur_len += 2
            if not pali_end:
				if s[i] == s[i-1]:
					cur_len = 2
					pali_end = True
					same = True
				elif s[i] == s[i-2]:
					cur_len = 3
					pali_end = True
					same = False
            i += 1
        if pali_end and max_len < cur_len:
            return s[-cur_len:]
        else:
			return s[max_index-max_len:max_index]