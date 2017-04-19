# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl = ListNode(0)
        tmp = rl
        l1_over = False
        l2_over = False
        while l1_over == False:
            if l2_over:
                if l1.val + tmp.val < 10:
                    tmp.val = l1.val + tmp.val
                    tmp.next = ListNode(0)
                else:
                    tmp.val = l1.val + tmp.val - 10
                    tmp.next = ListNode(1)
            else:
                if l1.val + l2.val + tmp.val < 10:
                    tmp.val = l1.val + l2.val + tmp.val
                    tmp.next = ListNode(0)
                else:
                    tmp.val = l1.val + l2.val + tmp.val - 10
                    tmp.next = ListNode(1)
            if l2.next == None:
                l2_over = True
            else:
                l2 = l2.next
            if l1.next == None:
                l1_over = True
                if l2_over and tmp.next.val == 0:
                    tmp.next = None
                else:
                    tmp = tmp.next
            else:
                l1 = l1.next
                tmp = tmp.next
        while l2_over == False:
            if l2.val + tmp.val < 10:
                tmp.val = l2.val + tmp.val
                tmp.next = ListNode(0)
            else:
                tmp.val = l2.val + tmp.val - 10
                tmp.next = ListNode(1)
            if l2.next == None:
                l2_over = True
                if tmp.next.val == 0:
                    tmp.next = None
            else:
                l2 = l2.next  
                tmp = tmp.next
        return rl