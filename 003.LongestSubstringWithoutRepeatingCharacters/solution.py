class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        char_dict = {}
        for i in range(len(s)):
            if char_dict.get(s[i]) == None or cur_len < i - char_dict[s[i]]:
                char_dict[s[i]] = i
                cur_len += 1
                if max_len < cur_len:
                    max_len = cur_len
            else:
                cur_len = i - char_dict[s[i]]
                char_dict[s[i]] = i
        return max_len
            
