from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = defaultdict(bool)
        for num in nums:
            if num in visited:
                return True
            visited[num] = True
        return False
        
        
