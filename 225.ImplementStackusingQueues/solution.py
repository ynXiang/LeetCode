#https://discuss.leetcode.com/topic/16847/python-solution-o-1-o-n-for-push-48ms

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queuePush(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tmp = []
        while not self.queueIsEmpty():
            tmp.append(self.queuePop())
        for v in tmp[:-1]:
            self.queuePush(v)
        return tmp[-1]

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        ans = self.pop()
        self.queuePush(ans)
        return ans

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queueIsEmpty()
        
    def queuePush(self, x):
        self.stack.append(x)
        
    def queuePop(self):
        return self.stack.pop(0)
        
    def queuePeek(self):
        return self.stack[0]
        
    def queueSize(self):
        return len(self.stack)
        
    def queueIsEmpty(self):
        return not len(self.stack)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
