# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1.val
        while l1.next:
            n1 *= 10
            l1 = l1.next
            n1 += l1.val
        n2 = l2.val
        while l2.next:
            n2 *= 10
            l2 = l2.next
            n2 += l2.val
        num = str(n1 + n2)
        ans = None
        for i in num[::-1]:
            newNode = ListNode(int(i))
            newNode.next = ans
            ans = newNode
        return ans
