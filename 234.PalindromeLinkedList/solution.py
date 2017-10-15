#https://discuss.leetcode.com/topic/18293/11-lines-12-with-restore-o-n-time-o-1-space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and slow and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        if rev or slow:
            return False
        else:
            return True
