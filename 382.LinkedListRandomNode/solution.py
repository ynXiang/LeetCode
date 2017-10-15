# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 1
        while head.next:
            head = head.next
            self.length += 1
        head.next = self.head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        k = random.randint(0, self.length-1)
        node = self.head
        while k > 0:
            node = node.next
            k -= 1
        return node.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
