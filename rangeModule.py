class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        for i in range(left, right):
            self.mySet.add(i)

    def queryRange(self, left: int, right: int) -> bool:
        for i in range(left, right):
            if i not in self.mySet:
                return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        for i in range(left, right):
            if i in self.mySet:
                self.mySet.remove(i)

# Example usage:
# obj = RangeModule()
# obj.addRange(left, right)
# param_2 = obj.queryRange(left, right)
# obj.removeRange(left, right)
