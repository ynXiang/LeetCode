# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            tmp = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = tmp
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        nullNode = RandomListNode(0)
        cur, resCur = head, nullNode
        while cur:
            resCur.next = cur.next
            resCur = resCur.next
            cur.next = resCur.next
            cur = cur.next
        return nullNode.next
