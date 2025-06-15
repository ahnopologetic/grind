import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = []

        for stone in stones:
            heapq.heappush(result, -stone)
        
        while result:
            s1 = -heapq.heappop(result)
            if not result:
                return s1
            
            s2 = -heapq.heappop(result)
            if s1 > s2:
                heapq.heappush(result, s2 - s1)
        
        return 0
        


            

