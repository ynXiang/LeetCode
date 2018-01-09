class DLL(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.head = DLL(0)
        self.tail = DLL(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            cur = self.data[key][1]
            if cur.next: cur.next.prev = cur.prev
            if cur.prev: cur.prev.next = cur.next
            cur.next, cur.prev = self.head.next, self.head
            cur.next.prev = cur.prev.next = cur
            return self.data[key][0]
        else: return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0: return
        if key in self.data:
            self.data[key] = (value, self.data[key][1])
        else:
            self.data[key] = (value, DLL(key))
        if len(self.data) == self.capacity + 1:
            del self.data[self.tail.prev.val]
            self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev
        self.get(key)
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
