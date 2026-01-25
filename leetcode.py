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
        self.dict = {}
    
    def remove(self, key):
        node = self.dict[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.dict[key]
    
    def insert(self, key, val):
        self.dict[key] = ListNode(key, val, self.head.next, self.head)
        self.dict[key] = self.head.next.prev
        self.head.next = self.dict[key]


    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(key)
            self.put
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(key)
            self.put(key, value)
            return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)