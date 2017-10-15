# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        i = 0
        while i < length - k % length:
            cur = cur.next
            i += 1
        res, cur.next = cur.next, None
        return res
