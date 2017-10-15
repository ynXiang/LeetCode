# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        origin = leftCur = ListNode(None)
        leftCur.next = head
        pre = leftCur
        while cur.next:
            if cur.val < x:
                pre.next = cur.next
                tmp = leftCur.next
                leftCur.next = ListNode(cur.val)
                leftCur = leftCur.next
                leftCur.next = tmp
                if pre.next == leftCur:
                    pre = pre.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        if cur.val < x:
            pre.next = cur.next
            tmp = leftCur.next
            leftCur.next = ListNode(cur.val)
            leftCur = leftCur.next
            leftCur.next = tmp
        return origin.next
