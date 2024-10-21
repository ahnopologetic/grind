class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            hashmap[num] = idx
        
        for idx, num in enumerate(nums):
            search = target - num
            if search in hashmap and hashmap[search] != idx:
                return [idx, hashmap[search]]
        
        return []

