class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.timeAccessed = {}
        self.time = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache["MRU"] = key
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < capacity + 1:
            self.cache[key] = value
        
        else:
            print("here")
            MRU = self.cache["MRU"]
            del self.cache["MRU"]
            keys = self.cache.keys()

            for i in self.cache.keys():
                if i != MRU:
                    LRU = i
            del self.cache[LRU]
            self.cache[key] = value
            self.cache["MRU"] = key
            self.timeAccessed[key] = self.time
        self.time += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)