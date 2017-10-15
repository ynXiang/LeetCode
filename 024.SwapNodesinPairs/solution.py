# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        origin = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            tmp1, tmp2 = cur.next, cur.next.next
            cur.next, tmp1.next, tmp2.next = tmp2, tmp2.next, tmp1
            cur = cur.next.next
        return origin.next
