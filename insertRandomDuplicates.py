class RandomizedCollection:
    def __init__(self):
        self.map = defaultdict(set)
        self.list = []
        
    def insert(self, val: int) -> bool:
        self.map[val].add(len(self.list))
        self.list.append(val)
        return len(self.map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.map[val]:
            return False
        lastVal = self.list[-1]
        index = self.map[val].pop()
        self.list[index] = lastVal
        self.map[lastVal].add(index)
        self.map[lastVal].discard(len(self.list) - 1)
        self.list.pop()
        return True
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()