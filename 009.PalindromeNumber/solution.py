class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        string = str(x)
        reverse_string = string[::-1]
        return string == reverse_string
