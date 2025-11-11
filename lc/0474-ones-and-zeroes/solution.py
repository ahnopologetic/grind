from functools import cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        costs = [(s.count("0"), s.count("1")) for s in strs]

        for zero, one in costs:
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zero][j-one])
        
        return dp[m][n]
