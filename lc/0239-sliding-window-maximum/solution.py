class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result = []
        # start = 0
        # end = k - 1

        # for i in range(len(nums)-k+1):
        #     result.append(max(nums[start+i:end+i+1]))
        
        # return result

        d = deque()
        out = []

        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            
            d.append(i)

            if d[0] == i - k:
                d.popleft()
            
            if i >= k-1:
                out.append(nums[d[0]])
        return out
