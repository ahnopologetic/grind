class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            total_sum = max(total_sum, current_sum)
        return total_sum
            

        
