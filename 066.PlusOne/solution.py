class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in reversed(range(len(digits))):
            if add == 1 and digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1]+digits
            else:
                digits[i] += 1
                return digits
