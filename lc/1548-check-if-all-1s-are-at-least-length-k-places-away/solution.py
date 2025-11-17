class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        stack = []
        for idx, num in enumerate(nums):
            if num == 0:
                continue
            if stack and idx - stack[-1] <= k:
                return False
            
            stack.append(idx)
        
        return True
        
