#https://discuss.leetcode.com/topic/43463/1-2-lines-python-ruby

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = []
        vowel = []
        for i,v in enumerate(s):
            if v in ["a","e","i","o","u","A","E","I","O","U"]:
                index.append(i)
                vowel.append(v)
        ans = list(s)
        for i,v in enumerate(vowel[::-1]):
            ans[index[i]] = v
        return "".join(ans)
