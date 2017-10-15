# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        null = ListNode(-1)
        null.next = head
        head = null
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return null.next
