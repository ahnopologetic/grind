class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            compl = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == compl:
                    return [i, j]                


        return []
        
