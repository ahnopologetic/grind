class Solution:
    def rob(self, nums: List[int]) -> int:
        # same method as the other quesetion
        # adding 0 at the end, traversing reverse picking the max

        # nums.append(0)

        # for i in range(len(nums) - 4, -1, -1):
        #     nums[i] += max(nums[i+2], nums[i+3])
        
        # return max(nums[0], nums[1])



        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]

        if len(nums) == 1:
            return dp[0]

        dp[1] = max(nums[0], nums[1])

        
        if len(nums) == 2:
            return max(dp[0], dp[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]
