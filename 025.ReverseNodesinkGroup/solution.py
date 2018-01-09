# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        nullNode = ListNode(0)
        nullNode.next = head
        cur = nullNode
        while self.exists(cur, k):
            cur = self.reverse(cur, k)
        return nullNode.next
    
    def exists(self, head, k):
        cur = head
        if not cur:
            return False
        while k > 0 and cur.next:
            cur = cur.next
            k -= 1
        return k == 0
    
    def reverse(self, head, k):
        firstHead, firstTail, second = head.next, head.next, head.next.next
        for i in xrange(k-1):
            head.next, firstTail.next, second.next = second, second.next, firstHead
            firstHead, second = head.next, firstTail.next
        return firstTail
