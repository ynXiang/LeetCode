class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.minimum = x

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack = ListNode(x)
        else:
            new = ListNode(x)
            new.prev = self.stack
            new.minimum = self.stack.minimum if self.stack.minimum < x else x
            self.stack = new

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        else:
            tmp = self.stack
            self.stack = self.stack.prev
            return tmp.val

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack.val
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
