from math import inf

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        minimumArea = inf
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    minimumArea = min(minimumArea, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))
        if minimumArea == inf:
            return 0
        return minimumArea