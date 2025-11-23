class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter()
        for num in nums:
            if c[num] >= 1:
                return True
            c[num] += 1
        
        return False
