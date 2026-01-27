class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def remove(self, key):
        node = self.dict[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.dict[key]

    def insert(self, key, val):
        next = self.head.next
        node = ListNode(key, val, next, self.head)
        next.prev = node
        self.head.next = node
        self.dict[key] = node

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
        if len(self.dict) > self.cap:
            self.remove(self.tail.prev.key)
        
        
