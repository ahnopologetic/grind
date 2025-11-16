from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # q = [(k, 0)] # node, time
        q = [(0, k)]
        dist = defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    new_time = time + w
                    heapq.heappush(q, (new_time, v))
            
        if len(dist) == n:
            return max(dist.values())
        return -1
                
        
