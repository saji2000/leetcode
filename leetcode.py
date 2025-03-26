class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:
            values = self.hashMap[key]
        else:
            return ""
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r)//2

            if values[mid][1] == timestamp:
                return values[mid][0]
            
            if values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0]
                l = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)