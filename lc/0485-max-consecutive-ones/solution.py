class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_sum += 1
            else:
                curr_sum = 0
            
            max_sum = max(max_sum, curr_sum)
        return max_sum
