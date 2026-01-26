class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}
    
    def remove(self, key):
        node = self.dict[key]

        prev = node.prev
        next = node.next
        if next:
            next.prev = prev

        prev.next = next
        del self.dict[key]
    
    def insert(self, key, val):
        next = self.head.next
        self.dict[key] = ListNode(key, val, next, self.head)

        if next:
            next.prev = self.dict[key] 
        self.head.next = self.dict[key]


    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict[key].val
            self.remove(key)
            self.insert(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(key)

        self.insert(key, value)
        if len(self.dict) > self.capacity:
            self.remove(self.tail.prev.key)

        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)