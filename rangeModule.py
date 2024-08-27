import bisect

class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        bisect.insort(self.intervals, [left, right])

        output = [self.intervals[0]]

        for start, end in self.intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        
        self.intervals = output
        
    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.intervals:
            if left >= start and right <= end:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        output = []

        for start, end in self.intervals:
            if end <= left or start >= right:
                output.append([start, end])
            else:
                if start < left:
                    output.append([start, left])
                if end > right:
                    output.append([right, end])
        self.intervals = output
# Example usage:
# obj = RangeModule()
# obj.addRange(left, right)
# param_2 = obj.queryRange(left, right)
# obj.removeRange(left, right)
