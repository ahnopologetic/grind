import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        curr_max = -999999
        hp = []
        heapq.heapify(hp)
        for _, val in enumerate(nums):
            curr = val
            if val > curr_max:
                heapq.heappush(hp, val)
            if len(hp) > k:
                heapq.heappop(hp)
        return heapq.heappop(hp)

