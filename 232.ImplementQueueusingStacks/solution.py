class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackPush(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmp = []
        for i in range(self.stackSize()):
            tmp.append(self.stackPop())
        ans = tmp.pop()
        for i in tmp[::-1]:
            self.stackPush(i)
        return ans

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmp = []
        for i in range(self.stackSize()):
            tmp.append(self.stackPop())
        ans = tmp[-1]
        for i in tmp[::-1]:
            self.stackPush(i)
        return ans

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stackIsEmpty()
    
    def stackPush(self, x):
        self.queue.append(x)
    
    def stackPop(self):
        return self.queue.pop()
        
    def stackPeek(self):
        return self.queue[-1]
        
    def stackSize(self):
        return len(self.queue)
        
    def stackIsEmpty(self):
        return not len(self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
