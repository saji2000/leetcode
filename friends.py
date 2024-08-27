from collections import defaultdict 

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int):
        logs = sorted(logs, key = lambda x: x[0])

        graph = defaultdict(set)

        for i in range(n):
            graph[i] = {i}
        
        for ts, p1, p2 in logs:
            graph[p1] = graph[p1].union(graph[p2])
            
            for p3 in graph[p1]:
                graph[p3] = graph[p1]
            
            if len(graph[p1]) == n:
                return ts
        
        return -1