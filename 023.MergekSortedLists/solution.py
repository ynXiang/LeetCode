# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        pq = [(lists[index].val, index) for index in xrange(len(lists)) if lists[index]]
        heapq.heapify(pq)
        nullNode = ListNode(0)
        last = nullNode
        while pq:
            smallest = heapq.heappop(pq)[1]
            last.next = lists[smallest]
            last = last.next
            lists[smallest] = lists[smallest].next
            if lists[smallest]:
                heapq.heappush(pq, (lists[smallest].val, smallest))
        return nullNode.next
