class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}


        def dp(i: int):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            
            elif i == 1 or i == 2:
                return 1
            
            else:
                result = dp(i-1) + dp(i-2) + dp(i-3)
                memo[i] = result
                return result


        return dp(n)

