# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        a = head.next
        b = head.next.next
        if not b:
            return False
        while a != b:
            a = a.next
            b = b.next
            if not a or not b:
                return False
            b = b.next
            if not b:
                return False
        return True
