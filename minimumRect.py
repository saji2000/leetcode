from math import inf

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashmap = {}

        for i in range(len(points)):
            if points[i][0] not in hashmap:
                hashmap[points[i][0]] = set()
            hashmap[points[i][0]].add(points[i][1])

        minimumArea = inf
        for i in range(len(points)):
            for j in range(len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                if x1 != x2 and y1 != y2:
                    if y1 in hashmap[x2] and y2 in hashmap[x1]:
                        minimumArea = min(minimumArea, abs(y1 - y2) * abs(x1 - x2))
        if minimumArea == inf:
            return 0
        return minimumArea