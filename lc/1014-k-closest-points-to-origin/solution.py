import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            heapq.heappush(heap, (sqrt(x**2 + y**2), [x, y]))
        
        for _ in range(k):
            _, coordinate = heapq.heappop(heap)
            result.append(coordinate)
        
        return result
        
