#https://discuss.leetcode.com/topic/86534/tiny-ruby-short-python-java-c

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Acount = 0
        Lcount = 0
        for i in s:
            if i == "A":
                Lcount = 0
                Acount += 1
                if Acount > 1:
                    return False
            elif i == "L":
                Lcount += 1
                if Lcount > 2:
                    return False
            else:
                Lcount = 0
        return True
