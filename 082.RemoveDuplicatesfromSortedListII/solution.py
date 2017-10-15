#https://discuss.leetcode.com/topic/5206/my-recursive-java-solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        origin = ListNode(None)
        origin.next = head
        pre, cur = origin, head
        duplicate = False
        while cur.next:
            if cur.next.val == cur.val:
                duplicate = True
                cur.next = cur.next.next
            else:
                if duplicate:
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                else:
                    cur = cur.next
                    pre = pre.next
                duplicate = False
        if duplicate:
            pre.next = None
        return origin.next
