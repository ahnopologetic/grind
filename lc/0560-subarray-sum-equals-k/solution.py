class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # two pointer
        # its o^2, but let's go
        
        # it is prefixed sum

        sub = {0: 1}
        total = result = 0
        for num in nums:
            total = total + num
            if total - k in sub:
                result += sub[total-k]
            sub[total] = 1 + sub.get(total, 0)
        
        return result
        
