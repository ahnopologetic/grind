class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_map = {}

        for _, num in enumerate(nums):
            num_map[num] = True
        
        for k, uniq_num in enumerate(num_map.keys()):
            nums[k] = uniq_num
        
        return len(num_map.keys())
        
